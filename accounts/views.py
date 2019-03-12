from django.shortcuts import render


def LoginView(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        form.save()
    else:
        form=LoginForm()

    return render(request,"registration/login.html",{"form":form})