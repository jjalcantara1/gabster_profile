from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import UserAccount
from testimonials.models import Testimonial


# Create your views here.

def home_screen_view(request, *args, **kwargs):
    context = {}  # allows to pass variables in the view
    return render(request, 'general/home.html', context)

def profile_view(request, username):

    user = get_object_or_404(UserAccount, username=username)
    testimonials_received = Testimonial.objects.filter(user_to=user).order_by('-createdAt')
    context = {
        'user': user,
        'person': request.user,
        'testimonials_received': testimonials_received,
    }
    return render(request, 'profile/profile.html', context)
