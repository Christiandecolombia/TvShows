from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Tvshow

####new#####
def new(request):
    return render(request,'allshows/new.html')

def create(request): 
    if request.method == "POST":
            errors = Tvshow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect ('/new'+id)
    else:
        Tvshow.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            date = request.POST['date'],
            desc = request.POST['desc']
            )
    newshow=Tvshow.objects.get(title=request.POST['title'])
    return redirect('/'+str(newshow.id))

####allshows####
def index(request):
    context = {
        "allshows":Tvshow.objects.all()
    }
    return render(request,'allshows/index.html',context)



####edit####
def edit(request,id):
    context= {
        "editshow":Tvshow.objects.get(id=id),
    }
 
    return render(request,'allshows/edit.html',context)

def editshow(request,id):
    if request.method== 'POST':
        errors = Tvshow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect ('/edit/'+id)
    else:
        if request.method == 'POST':
            edit=Tvshow.objects.get(id=id)
            edit.title=request.POST['title']
            edit.network = request.POST['network']
            edit.date = request.POST['date']
            edit.desc = request.POST['desc']
            edit.save()
        return redirect('/')


####view####
def view(request,id):
    context = {
        "allshows":Tvshow.objects.get(id=id)
    }
    return render(request,'allshows/view.html',context)

def delete(request,id):
    delete=Tvshow.objects.get(id=id)
    delete.delete()
    return redirect('/')

