from django.urls import path
from . import views

urlpatterns = [
	path('book', views.book, name="book"),
	path(r'form', views.my_form, name='form'),
	path('myappointments', views.myappointments, name='myappointments'),

]
