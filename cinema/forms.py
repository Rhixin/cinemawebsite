from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Account, Profile

class AccountForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['username','password']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fname', 'lname', 'birth_date', 'address']
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'password1', 'password2']

