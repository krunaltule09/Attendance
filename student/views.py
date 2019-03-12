from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Student
from django.urls import reverse

User=get_user_model()

@login_required
def HomePageView(request):
	return HttpResponseRedirect(reverse('index'))
 
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
