from django.urls import path
from . import views
from . views import home
urlpatterns=[path('',home,name='home'),
             path('add',views.add ,name='add')]