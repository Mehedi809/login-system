# from django import forms
# from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User

# class RegistrationForm(forms.Form):
#     username = forms.CharField(min_length=4, required=True)
#     email = forms.EmailField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput)
#     confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username).exists():
#             raise ValidationError("Username is already taken.")
#         return username

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password != confirm_password:
#             raise ValidationError("Passwords do not match.")
