#-*- coding: utf-8 -*-

from django.views.generic.edit import CreateView

from .models import *
from .forms import *

class UserCreate(CreateView):
    model = UserProfile
    form = UserForm
    fields = ['username', 'email', 'password', 'name']