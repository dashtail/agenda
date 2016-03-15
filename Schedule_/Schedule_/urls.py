"""
Definition of urls for Schedule_.
"""

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='home'),

    url(r'^Usuarios/', include('Schedule_.user.urls'), name ='projets'),
]
