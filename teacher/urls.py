from django.urls import path
from .views import Profile,RandomCodeGenerator,Button

app_name = 'teacher'

urlpatterns = [
      # path('',HomePageView,name='index'),
      path('profile/', Profile,name='profile'),
      
      path('code/', RandomCodeGenerator,name='requested'),
   ]