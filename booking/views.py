from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.utils.safestring import mark_safe
# Create your views here.


from .models import MyModel
from .forms import MyForm
 
def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'form.html', {'form': form})



def book(request):
	if not request.user.is_active:
		messages.info(request, 'Please login first')
		return redirect('login')
	
	if request.method=='POST':
		first_name = request.POST['first_name']
		email = request.POST['email']
		Text = request.POST['Text']
		Time = request.POST['Time']
		service = request.POST['service']
		barber = request.POST['barber']
		MyModel.objects.create(username=first_name,email=email,date=Text,time=Time,service=service,barber=barber)

		

		messages.info(request, "Appointment booked successfully, you can check your appointment details in")
		messages.info(request, mark_safe('<a href="booking/myappointments" style="color: rgba(50,205,50, 0.54);"> My appointments.</a>'))
		messages.info(request, "If date and time you picked isn't available, we'll pick the closest one to that you picked")
	return render(request, 'home.html')



def myappointments(request):

	MyModels = MyModel.objects.all()

	return render(request, 'myappointments.html', {'MyModels': MyModels})

