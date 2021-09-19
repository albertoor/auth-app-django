from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = (
			'username', 
			'email', 
			'password1',
			'password2'
		)

	# def save(self, commit=True):
	# 	user = super(SignUpForm, self).save(commit=False)
	# 	user.email = cleaned_data['email']

	# 	if commit:
	# 		user.save()

	# 	return user