from django.shortcuts import render, redirect
from .forms import MemberRegistrationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as generic_login


# Create your views here.
def login(request):
    form = AuthenticationForm()
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:  # above line returns None if Permission Denied.
                generic_login(request, user)
                return redirect('/')

    context = {'form':form}
    return render(request, 'login.html', context)


def register(request):
    """
    'Views' are functions that take an HTTP request
    as input and return an HTTP Response as output.
    llamas
    """
    if request.method == 'GET':
        user_form = UserCreationForm()
        member_form = MemberRegistrationForm()

    elif request.method == 'POST':
        querydict = request.POST
        user_form = UserCreationForm(data=querydict)
        member_form = MemberRegistrationForm(data=querydict)

        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save(commit=False)
            member = member_form.save(commit=False)

            user.save()
            member.user = user
            member.save()

            return redirect('/')

    context = {'member_form': member_form, 'user_form': user_form}
    return render(request, 'register.html', context)
