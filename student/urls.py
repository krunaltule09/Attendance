from django.urls import path
from .views import HomePageView

app_name = 'student'


urlpatterns = [
	path('', HomePageView,name='index'),


]