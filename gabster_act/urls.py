"""
URL configuration for gabster_act project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path  # para mainclude ung views ng posts app
from django.conf import settings
from django.conf.urls.static import static
from Post.views import *
from accounts.views import login_view, register_view, logout_view, post
from testimonials import views
from testimonials.views import *
from .views import *
from templates import *
# from general.views import home_screen_view
# from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('post/', post, name='post'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    #path('accounts/', include('accounts.urls')),
    #path('accounts/', include('allauth.urls')),
    re_path(r'^profile/(?P<username>[\w.@+-]+)/$', profile_view, name='profile'),
    # path('profile/', profile, name='profile'), #Addition so that the main page is your (logged in user) profile
    # path('profile/<str:username>', profile_view, name='profile_view'),

    # re_path(r'^testimonial/(?P<username>[\w.@+-]+)/$', TestimonialListView.as_view(), name='testimonial-list'),
    # re_path(r'^testimonial/(?P<username>[\w.@+-]+)/create/$', TestimonialDetailView.as_view(), name='testimonial-detail'),
    # re_path(r'^addtestimonials/(?P<username>[\w.@+-]+)/$', views.add_testimonial, name='add_testimonial'),
    path('addtestimonials/<str:user_to_username>/', views.add_testimonial, name='add_testimonial'),
    path('testimonials/<str:username>/', views.view_testimonials, name='view_testimonials'),
    # re_path(r'^testimonials/(?P<username>[\w.@+-]+)$', views.view_testimonials, name='view_testimonials'),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
                  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
