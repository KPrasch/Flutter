from django.conf.urls import url
from django.contrib import admin
from flutz.views import (timeline, create_flutt, search_flutts)
from accounts.views import register, login
from django.contrib.auth.views import logout


urlpatterns = [
    # Django Admin
    #url(r'^admin/', my_fake_keylogger), #TODO: Make fake django honeypot
    url(r'^admin/', admin.site.urls),

    # Flutz Application
    url(r'^$', timeline),
    url(r'^flutz/post/$', create_flutt),
    url(r'^flutz/search/$', search_flutts),

    # Accounts Application
    url(r'^accounts/register/$', register),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
]
