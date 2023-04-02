from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from datetime import date
from .models import Notes


# Create your views here.


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')


def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['PSW']
        user = authenticate(username=u, password=p)

        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    d = {'error': error}
    return render(request, 'login.html', d)


def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['Uname']
        p = request.POST['PSW']
        user = authenticate(username=u, password=p)

        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    d = {'error': error}
    return render(request, 'login_admin.html', d)


def signup1(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fastname']
        l = request.POST['lastname']
        c = request.POST['contacatnumber']
        e = request.POST['emailID']
        p = request.POST['password']
        b = request.POST['branch']
        r = request.POST['role']
        try:
            user = User.objects.create_user(
                username=e, password=p, first_name=f, last_name=l)
            Signup.objects.create(user=user, contact=c, branch=b, role=r)
            error = "no"
        except:
            error = "yes"

    d = {'error': error}
    return render(request, 'signup.html', d)


def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    pn = Notes.objects.filter(status="pending").count()
    an = Notes.objects.filter(status="Accept").count()
    rn = Notes.objects.filter(status="Reject").count()
    alln = Notes.objects.all().count()
    d = {'pn': pn, 'an': an, 'rn': rn, 'alln': alln}
    return render(request, 'admin_home.html', d)


def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    d = {'data': data, 'user': user}
    return render(request, 'profile.html', d)


def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    error = False
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        b = request.POST['branch']
        user.first_name = f
        user.last_name = l
        data.contact = c
        data.branch = b
        user.save()
        data.save()
        error = True
    d = {'data': data, 'user': user, 'error': error}
    return render(request, 'edit_profile.html', d)


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['Confirm']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "no"
        else:
            error = "yes"
        d = {'error': error}
        return render(request, 'change_password.html', d)
    else:
        return render(request, 'change_password.html')


'''
def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        b = request.POST['branch']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['description']

        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u, uploadindate=date.today(), branch=b, subject=s, notesfile=n, filetype=f,
                                 description=d, status='pending')
            error = "no"
        except:
            error = "yes"

        d = {'error': error}
        return render(request, 'upload_notes.html', d)
    else:
        return render(request, 'upload_notes.html')
 '''


def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        b = request.POST['branch']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['description']
        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u, uploadingdate=date.today(), branch=b, subject=s, notesfile=n,
                                 filetype=f, description=d, status='pending')
            error = "no"
        except:
            error = "yes"
    return render(request, 'upload_notes.html', locals())


'''

def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user=user)

    d = {'notes': notes}
    return render(request, 'view_mynotes.html', d)

'''


def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    notes = Notes.objects.filter(user=user)
    return render(request, 'view_mynotes.html', {'notes': notes})


def delete_mynotes(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_mynotes')


def view_users(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    users = Signup.objects.all()
    return render(request, 'view_users.html', {'users': users})


def delete_users(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('view_users')


def pending_nots(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="pending")
    return render(request, 'pending_notes.html', {'notes': notes})


def assign_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        s = request.POST['status']
        try:
            notes.status = s
            error = "yes"
        except:
            error = "yes"
    d = {'notes': notes, 'error': error}
    return render(request, 'assign_status.html', d)


def assign_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        s = request.POST.get('Status')
        try:
            notes.status = s
            notes.save()
            error = "no"
        except:
            error = "yes"
    d = {'notes': notes, 'error': error}
    return render(request, 'assign_status.html', d)


def accepted_nots(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="Accept")
    return render(request, 'accepted_nots.html', {'notes': notes})


def rejected_nots(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="Reject")
    return render(request, 'rejected_nots.html', {'notes': notes})


def all_nots(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.all()
    return render(request, 'all_nots.html', {'notes': notes})


def delete_nots(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('all_nots')


def view_all_nots(request):
    if not request.user.is_authenticated:
        return redirect('login')
    notes = Notes.objects.filter(status='Accept')
    return render(request, 'view_all_nots.html', {'notes': notes})
