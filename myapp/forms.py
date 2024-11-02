from django import forms


# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(
#         max_length=150,
#         validators=[RegexValidator(r'^[\w.@+-]+$', 'Enter a valid username.')],
#         error_messages={'required': 'Username is required.'}
#     )
#     name = forms.CharField(
#         max_length=100,
#         error_messages={'required': 'Name is required.'}
#     )
#     email = forms.EmailField(
#         validators=[EmailValidator(message='Enter a valid email address.')],
#         error_messages={'required': 'Email is required.'}
#     )
#     phone = forms.CharField(
#         max_length=15,
#         validators=[RegexValidator(r'^\d{10,15}$', 'Enter a valid phone number.')],
#         error_messages={'required': 'Phone number is required.'}
#     )
#     address = forms.CharField(
#         widget=forms.Textarea,
#         error_messages={'required': 'Address is required.'}
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput,
#         min_length=8,
#         error_messages={
#             'required': 'Password is required.',
#             'min_length': 'Password must contain at least 8 characters.'
#         }
#     )
#     password_confirmation = forms.CharField(
#         widget=forms.PasswordInput,
#         label='Confirm Password',
#         error_messages={'required': 'Please confirm your password.'}
#     )

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password_confirmation = cleaned_data.get('password_confirmation')

#         if password and password_confirmation and password != password_confirmation:
#             raise forms.ValidationError("Passwords do not match.")

#         return cleaned_data
