from django.shortcuts import render,redirect
from django.http import HttpResponse






def HomePageView(request):
	return render(request,"student/index.html")