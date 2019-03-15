from django.urls import path
from .views import HomePageView,Profile

app_name = 'student'


urlpatterns = [
	# path('', HomePageView,name='index'),
	path('profile/', Profile,name='profile'),
	


]