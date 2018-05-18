from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản',max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mật khẩu', max_length=16,widget=forms.PasswordInput())
    repass = forms.CharField(label='Nhập Lại Mật khẩu', max_length=16,widget=forms.PasswordInput())

    def clean_repass(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            repass = self.cleaned_data['repass']
            if password == repass and password:
                return repass
        raise forms.ValidationError('Mật khẩu không phù hợp')
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Tên tài khoản có kí tự đặc biệt!')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Tên tài khoản đã tồn tại!')
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])

