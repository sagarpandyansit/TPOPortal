from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(max_length=256,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'name':'email',
                                }
                            ))
    password = forms.CharField(max_length=32,
                               widget=forms.PasswordInput(
                                   attrs={
                                      'class':'form-control',
                                      'id':'password',
                                       'name':'password',
                                }))

    def clean(self, *args, **kwargs):
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not email and not password:
            raise forms.ValidationError('You can not leave fields blank.')

class RegistrationForm(forms.Form):
    fullname = forms.CharField(max_length=256)
    course = forms.CharField(max_length=256)
    semester = forms.IntegerField()
    department = forms.CharField(max_length=256)
    password = forms.CharField(widget=forms.PasswordInput)
    mobno = forms.CharField(max_length=10)

    def clean(self , *args , **kwargs):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not email and not password:
            raise forms.ValidationError('You can not leave fields blank.')
