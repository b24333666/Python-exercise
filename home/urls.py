from django.urls import path
from . import views
app_name = "home"
urlpatterns = [
     #http://localhost:8000/
    path('',views.index,name='index'),
    #http://localhost:8000/about
    path('aboutxyz/',views.about,name='aboutme'),
    #http://localhost:8000/contact
    path('contact/',views.contact,name='contact'),
    path('contact/<str:name>',views.contact1,name='contact1'),
    path('upload/',views.uploaddata,name="uploadfile")    
   

]

