from django.shortcuts import render, redirect
from .forms import FluttForm, SearchForm
from .models import Flutt
from django.contrib.auth.decorators import login_required


def timeline(request):
    all_flutts = Flutt.objects.order_by('created')[0:10]
    search_form = SearchForm()
    context = {'flutts': all_flutts, 'form': search_form}
    return render(request, 'timeline.html', context)


# @login_required
def create_flutt(request):

    if request.method == "POST":
        form = FluttForm(data=request.POST)
        if form.is_valid():
            flutt = form.save(commit=False)
            flutt.save()
            return redirect('/')

    elif request.method == "GET":
        form = FluttForm()

    context = {'form': form}
    return render(request, 'create_flutt.html', context)


def search_flutts(request):
    if request.method == 'GET':
        search_item = request.GET['query_text']
        flutts = Flutt.objects.filter(body__icontains=search_item)
        context = {'flutts': flutts}
        return render(request, 'timeline.html', context)


def frogs(request):
    context = {}
    return render(request, 'frogs.html', context)
