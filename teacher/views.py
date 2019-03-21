from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Teacher
from django.urls import reverse
from django.http import HttpResponseRedirect
import random
import string
from accounts.models import Panel
from .models import SecretCode
from django.utils import timezone


User=get_user_model()

# @login_required
# def HomePageView(request):
#   return HttpResponseRedirect(reverse('teacher:pr'))
 
@login_required
def Profile(request):
    userid=request.user.id
    user=User.objects.get(id=userid)
    teacher=Teacher.objects.get(user=user)
    context={
    'erp':user.username,
    'name':(teacher.first_name+"\t"+teacher.last_name),
    'subject':teacher.subject,
        }

    return render(request,"teacher/profile.html",context)


@login_required
def RandomCodeGenerator(request,panel_number):

    chars =string.digits
    size = 8
    code=random_string_generator(size, chars)
    code_obj=SecretCode()
    code_obj.code=code
    code_obj.teacher_username=request.user.username
    panel=Panel.objects.get(panel_number=panel_number)
    code_obj.panel=panel
    code_obj.date_time_created=timezone.now()
    code_obj.save()
    context={
    'code':code,
    }
    # return HttpResponseRedirect(reverse("", kwargs={'pk': pk}))
    return render(request,'teacher/code.html',context)

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))



def Button(request):
    return render(request, 'teacher/button.html',{})


def PanelListView(request):
    list_of_panels=Panel.objects.all()
    context={
    'panel_list':list_of_panels,
    }
    return render(request,"teacher/panel_list.html",context)