from django.urls import path
from .views import Profile,RandomCodeGenerator,Button,PanelListView

app_name = 'teacher'

urlpatterns = [
      # path('',HomePageView,name='index'),
      path('panels/', PanelListView,name='panel_list'),
      path('code/<panel_number>/', RandomCodeGenerator,name='requested'),
   ]