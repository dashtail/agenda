#-*- coding: utf-8 -*-

from django import forms

from .models import UserProfile

class UserForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def save(self, commit=True):
        import pdb;pdb.set_trace()
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = UserProfile
        fields = []
        exclude = []
        widgets = {
            'password': forms.PasswordInput(),
        }