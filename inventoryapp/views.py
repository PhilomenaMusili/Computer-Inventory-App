from django.shortcuts import render, redirect
from .forms import ComputerForm, ComputerSearchForm
from .models import Computer
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, "home.html", context)

def computer_entry(request):
    title = 'Add Computer'
    form = ComputerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form.save_m2m()
        return redirect('/computer_list')
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "computer_entry.html", context)

def computer_list(request):
    title = 'List of all computers'
    queryset = Computer.objects.all()
    form = ComputerSearchForm(request.POST or None)
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Computer.objects.all().order_by('-timestamp').filter(computer_name__icontains=form['computer_name'].value(),users_name__icontains=form['users_name'].value())
        context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    return render(request, "computer_list.html", context)

def computer_edit(request, id=None):  
    instance = get_object_or_404(Computer, id=id)
    form = ComputerForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        return redirect('/computer_list')
    
    context = {
        "title": 'Edit ' + str(instance.computer_name),
        "instance": instance,
        "form": form,
    }
    return render(request, "computer_entry.html", context)

def computer_delete(request, id=None):
   instance = get_object_or_404(Computer, id=id)
   instance.delete()
   return redirect("computer_list")