from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm, AccountAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from accounts import *
from django.views import View
from templates import *
from accounts.models import UserAccount
from django.shortcuts import render, get_object_or_404


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f'You are already authenticated as {user.email}.')
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get('next')
            if destination:  # if destination is not equal to none
                return redirect(destination)
            return redirect('home')
        else:
            context['registration_form'] = form

    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request, *args, **kwargs):
    # form = AccountAuthenticationForm(request.POST)
    context = {}

    user = request.user
    if user.is_authenticated:
        # return redirect('profile')
        return redirect('profile_view')

    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        print(form.non_field_errors())
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                # destination = kwargs.get('next')
                if destination:
                    return redirect(destination)
                return redirect('profile', request.user.username)
                # return redirect('profile_view')
            else:
                form = AccountAuthenticationForm()

                context['login_form'] = form
    form = AccountAuthenticationForm(request.POST)
    return render(request, 'accounts/login.html', {'form':form})


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect

# def post(request):
#     return render(request, "posts/post.html", {})



