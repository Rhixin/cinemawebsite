from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Account, Profile

class AccountForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['username','password']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'block w-full border border-gray-300 rounded-md p-2 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'block w-full border border-gray-300 rounded-md p-2 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Password'
        })
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fname', 'lname', 'birth_date', 'address']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fname'].widget.attrs.update({
            'class': 'block w-full border border-gray-300 rounded-md p-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'First Name'
        })
        self.fields['lname'].widget.attrs.update({
            'class': 'block w-full border border-gray-300 rounded-md p-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Last Name'
        })
        self.fields['birth_date'].widget.attrs.update({
            'class': 'block w-full border border-gray-300 rounded-md p-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Birth Date (YYYY-MM-DD)'  
        })
        self.fields['address'].widget.attrs.update({
            'class': 'block w-full border border-gray-300 rounded-md p-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Address'
        })
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'password1', 'password2']
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'block w-full border border-gray-300 rounded-md p-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'block w-full border border-gray-300 rounded-md p-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'block w-full border border-gray-300 rounded-md p-2 mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Confirm Password'
        })

