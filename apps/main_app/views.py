from django.shortcuts import render, redirect
from .models import Contact, Winter_Jubilee, SSOT, Message_Board
from django.contrib import messages

def home(request):
    if request.session.get('user_id'):
        context = {
            'logged_in_user':request.session.get('user_id')
        }
        return render(request, "main_app/index.html", context)
    else:
        return render(request, "main_app/index.html")

def add_contact(request):
    errors = Contact.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Contact.objects.create(name=request.POST['name'], email=request.POST['email'], message=request.POST['message'])
        messages.success(request, "Thank you for your submission")
        return redirect('/')

def display_ssot(request):
    if request.session.get('user_id'):
        context = {
            'logged_in_user':request.session.get('user_id')
            }
        return render(request, "main_app/display_ssot_form.html", context)
    else:
        return render(request, "main_app/display_ssot_form.html")

def submit_ssot(request):
    errors = SSOT.objects.form_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/display_ssot')
    else:
        SSOT.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], gender=request.POST['gender'], need_transportation=request.POST['need_transportation'], going_to=request.POST['going_to'])
        messages.success(request, "Your submission was successful. Proceed to make payment to complete registration.")
        return redirect('/display_ssot')


def display_winter_jubilee(request):
    if request.session.get('user_id'):
        context = {
            'logged_in_user':request.session.get('user_id')
            }
        return render(request, "main_app/display_winter_jubilee_form.html", context)
    else:
        return render(request, "main_app/display_winter_jubilee_form.html")



def submit_winter_jubilee(request):
    errors = Winter_Jubilee.objects.form_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/display_winter_jubilee')
    else:
        Winter_Jubilee.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], gender=request.POST['gender'], need_transportation=request.POST['need_transportation'], going_to=request.POST['going_to'])
        messages.success(request, "Your submission was successful. Proceed to make payment to complete registration.")
        return redirect("/display_winter_jubilee")


def home_meetings(request):
    if request.session.get('user_id'):
        context = {
            'logged_in_user':request.session.get('user_id')
            }
        return render(request, "main_app/home_meetings.html", context)
    else: 
        return render(request, "main_app/home_meetings.html")


def announcements(request):
    context = {
        "all_messages": Message_Board.objects.all().order_by("-created_at"),
        'logged_in_user':request.session.get('user_id')
    }
    return render(request, "main_app/announcement_board.html", context)

def post_announcement(request):
    errors = Message_Board.objects.message_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/announcements')
    else:
        Message_Board.objects.create(name=request.POST['name'], message=request.POST['message'])
        # messages.success(request, "Your message has been posted")
    return redirect("/announcements")

