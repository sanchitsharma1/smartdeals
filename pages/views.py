from django.shortcuts import render

# Create your views here.

def home_view(request):

    return render(request, 'index.html', {})

def about_view(request):

    return render(request, 'about.html', {})

def contact_view(request):

    return render(request, 'contact.html', {})

def login_view(request):

    return render(request, 'login.html', {})

def signup_view(request):

    return render(request, 'signup.html', {})