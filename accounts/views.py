from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from django.contrib.auth import authenticate, login


def signup(request):
	form_class = SignUpForm
	
	form = form_class(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('login')


	return render(request, 'registration/signup.html', {'form': form})


# def password_reset_request(request):
# 	if request.method == 'POST'
# 		domain = request.headers['Host']
# 		password_reset_form = PasswordResetForm(request.POST)

# 		if password_reset_form.is_valid():
# 			data = password_reset_form.cleaned_data['email']
# 			associated_users = User.objects.filter(Q(email=data))

# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "Password Reset Requested"
# 					email_template_name = ''


