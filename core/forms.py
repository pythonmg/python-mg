from django import forms
from django.contrib.auth.models import User


class CreateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='First name')
    email = forms.EmailField(label='Email address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password', 'password2')

    def clean_password2(self):
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['password2']
        if pass1 != pass2:
            raise forms.ValidationError(
                'Password does not match, type the password again'
            )
        return pass1

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'E-mail already registered, enter another e-mail'
            )
        return email

    def save(self, commit=False):
        user = super(CreateUserForm, self).save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
