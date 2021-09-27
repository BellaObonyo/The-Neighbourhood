from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import NeighborHood,Business,Post,Profile

class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=100, help_text='Last Name')
  last_name = forms.CharField(max_length=100, help_text='Last Name')
  email = forms.EmailField(max_length=150, help_text='Email')

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class CreateNeighborHoodForm(forms.ModelForm):
  class Meta:
    model = NeighborHood
    fields = ['name','location','description','population','police_contact','hospital_contact','image']

class CreateBusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = ('name','description','image','email')

class CreatePostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title','post','image')

class UpdateBusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = ['name','description','image','email']

class UpdatePostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title','post','image']

class UpdateProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['first_name','last_name','bio','profile_picture','location']

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']

class UpdateNeighborhoodForm(forms.ModelForm):
  class Meta:
    model = NeighborHood
    fields = ['name','location','description','population','police_contact','hospital_contact','image']