from django.shortcuts import render, redirect
from users_app.models import User

# Create your views here.
def postingForm(request):
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    email = request.POST['email_address']
    ageIs = request.POST['age']

    User.objects.create(first_name=fname, last_name=lname, email_address=email, age=ageIs)



    return redirect ('/')


def index(request):
    context = {
        "Users": User.objects.all()
    }
    return render (request, "index.html",context)

# "allUsers":User.objects.all()