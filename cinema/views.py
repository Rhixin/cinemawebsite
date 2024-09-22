from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import AccountForm, ProfileForm, SignUpForm
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
                request.session['user_name'] = username
                return redirect('home')  
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AccountForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required
def go_home(request):
    user_name = request.session.get('user_name', None)
    
    return render(request, 'home.html', {'user_name': user_name})

def authView(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if signup_form.is_valid() and profile_form.is_valid():
            
            account = signup_form.save() 
            profile = profile_form.save(commit=False)
            profile.account = account 
            profile.save()

            login(request, account)

            return redirect('home')  
    else:
        signup_form = SignUpForm()
        profile_form = ProfileForm()

    return render(request, 'registration/signup.html', {
        'signup_form': signup_form,
        'profile_form': profile_form
    })