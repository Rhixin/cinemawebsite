from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import AccountForm, ProfileForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = AccountForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            account = authenticate(request, username=username, password=password)

            if account is not None:
                login(request, account)
                return redirect('home')  # Redirect to the home page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AccountForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required
def go_home(request):
    return render(request, 'home.html')

def authView(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if signup_form.is_valid() and profile_form.is_valid():
            # Save the Account
            account = signup_form.save()  # This handles password hashing
            # Save the Profile (link it to the account)
            profile = profile_form.save(commit=False)
            profile.account = account  # Link the profile to the newly created account
            profile.save()

            # Log the user in after sign up
            login(request, account)

            return redirect('home')  # Redirect to the home page or wherever you need
    else:
        signup_form = SignUpForm()
        profile_form = ProfileForm()

    return render(request, 'registration/signup.html', {
        'signup_form': signup_form,
        'profile_form': profile_form
    })