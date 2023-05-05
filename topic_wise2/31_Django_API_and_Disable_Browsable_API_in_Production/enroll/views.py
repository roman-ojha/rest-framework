from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Add new student & Show students


def add_and_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            user = User(name=name, email=email, password=password)
            user.save()
            # fm.save()
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    students = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'students': students})

# Delete student


def delete_student(request, id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        user.delete()
        return HttpResponseRedirect('/')


def update_student(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatestudent.html', {'form': fm})
