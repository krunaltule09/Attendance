
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect


User=get_user_model()

@login_required
def Home(request):

    userid =request.user.id 
    user1=User.objects.get(id=userid)
    if(user1.username[:4]=='1032'):
        return HttpResponseRedirect(reverse('student:profile'))
    elif(user1.username[:4]=='1035'):
        return HttpResponseRedirect(reverse('teacher:panel_list'))
    else:
        return HttpResponse('<h1>Access not allowed</h1>')


    return render(request, 'index.html',context)



def LoginView(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        form.save()
    else:
        form=LoginForm()

    return render(request,"registration/login.html",{"form":form})