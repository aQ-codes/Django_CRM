#your model forms goes here
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User  #default django user  model that we see in admin panel

from .models import Order , Customer

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']


class OrderForm(ModelForm):
    class Meta:
        #minimum of two fields required
        model = Order #which model to build form for
        fields = '__all__'
       
class CreateuserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #you can refer the doc to get the name of the fields  