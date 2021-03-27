from django import forms
from .models import MyModel
 
class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["username", "email","date","time","service","barber",]
    labels = {'username': "Name", "email": "Email", "date": "Book Your Date(YYYY-MM-DD)", "time": "Book Your Time", "service": "Services", "barber": "Barbers",}