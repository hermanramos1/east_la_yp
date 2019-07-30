from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt

def display_login_registration(request):
    context = {
        "current_user":request.session.get('user_id')
    }
    return render(request, "login_registration/index.html", context)

def register(request): 

    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/display_login_registration")
    else:
        if request.method == "POST":
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed_pw)
            request.session['user_id'] = new_user.id
            context = {
                'first_name' : new_user.first_name
            }
            return redirect("/word_feed")
         

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/display_login_registration")
    else:
        if request.method == "POST":
            matching_users = User.objects.filter(email = request.POST['email'])
            if matching_users:
                user = matching_users[0]
            else:
                messages.error(request, "Incorrect Email")
                return redirect('/display_login_registration')
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/word_feed')
            else:
                messages.error(request, "Incorrect password")
                return redirect('/display_login_registration')



    