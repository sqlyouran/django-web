# -*- coding: utf-8 -*-
import xadmin
from models import User
from django import forms
from django.contrib.auth.models import Group, Permission


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'is_active', 'is_superuser', 'is_editor')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("密码不一致")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserAdmin(object):
    form = UserCreationForm
    model_icon = 'fa fa-cog'
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_editor',)
    list_filter = ("is_staff", 'is_superuser', 'is_editor',)
    search_fields = ('username',)
    ordering = ('username',)
    list_per_page = 20
    show_bookmarks = False
    list_export = ('xls', 'xml', 'json', 'csv')
    list_editable = ['is_superuser', 'is_staff', 'is_editor']


xadmin.site.unregister(User)
xadmin.site.register(User, UserAdmin)
xadmin.site.unregister(Group)
xadmin.site.unregister(Permission)
