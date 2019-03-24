from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Student
from accounts.models import Panel,Subject
from teacher.models import SecretCode,Teacher
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import StudentAttendanceForm
from django.utils import timezone



# subjects={
#     "OS":"CS121",
#     "MMC":"CS212",
#     "SEPM":"CS299",
#     "DS2":"CS313",
#     "IC":"CS412"
# }


User=get_user_model()

@login_required
def HomePageView(request):
    return HttpResponseRedirect(reverse('student:profile'))
 
@login_required
def Profile(request):
    userid=request.user.id
    user=User.objects.get(id=userid)
    student=Student.objects.get(user=user)
    context={
    'erp':user.username,
    'name':(student.first_name+"\t"+student.last_name),
    'panel':student.panel,
    'rollnumber':student.roll_number,
    'os':student.att_os,
    'mmc':student.att_mmc,
    'ds2':student.att_ds2,
    'sepm':student.att_sepm,
    'ic':student.att_ic
    }

    return render(request,"student/profile.html",context)


def SubjectAttendance(request):

    if request.method=="POST":
        form=StudentAttendanceForm(request.POST)
        if form.is_valid():
            entered_code=form.cleaned_data["code"] 
            userid=request.user.id
            user=User.objects.get(id=userid)
            student=Student.objects.get(user=user)
            student_panel=student.panel


            date_today=timezone.now().date()          #getting date from user side
            time_now=timezone.now().time()
            code_list=SecretCode.objects.filter(date_time_created__date=timezone.now().date())
            for i in code_list:
                if(i.panel==student_panel):
                    
                    if(i.code==entered_code):
                        teacher_erp=i.teacher_username
                        user_teacher=User.objects.get(username=teacher_erp)
                        
                        teacher=Teacher.objects.get(user=user_teacher)
                        
                        sub_id=teacher.subject
                        
                        subject=Subject.objects.get(name=sub_id)
                        sub_name=subject.name
                        if(sub_name=="OS"):
                            student.att_os+=1
                        elif(sub_name=="DS2"):
                            student.att_ds2+=1
                        elif(sub_name=="MMC"):
                            student.att_mmc+=1
                        elif(sub_name=="SEPM"):
                            student.att_sepm+=1
                        else:
                            student.att_ic+=1
                        
                    student.save()
            return HttpResponseRedirect(reverse("student:profile"))
    else:
        form=StudentAttendanceForm()
        context={
        "form":form
        }
        return render(request,"student/enterCode.html",context)