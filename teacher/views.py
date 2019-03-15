from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Teacher
from django.urls import reverse
from django.http import HttpResponseRedirect
import random
import string

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
def RandomCodeGenerator(request):
    chars = string.ascii_letters + string.digits
    size = 12
    code=random_string_generator(size, chars)
    return render(request,'teacher/code.html',{'code':code})


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

    chars = string.ascii_letters + string.digits
    size = 12

    print(chars)
    print('Random String of length 12 =', random_string_generator(size, chars))

def Button(request):
    return render(request, 'teacher/button.html',{})
