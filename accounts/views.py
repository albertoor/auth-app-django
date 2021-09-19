from django.shortcuts import render, redirect

# Create your views here.
# from django.urls import reverse_lazy
from accounts.forms import SignUpForm
from django.views import generic
from django.contrib.auth import authenticate, login

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('login')
		else:
			form = SignUpForm()
		return render(request, 'registration/signup.html', {'form': form})