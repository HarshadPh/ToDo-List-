from django import views
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from matplotlib.style import context
from home.models import *
from .form import DocumentForm


# Create your views here.

def home(request):
    context = {'success': False}

    if request.method=="POST":
        #Handle the form
        title= request.POST['title']
        desc= request.POST['desc']
        form = DocumentForm(request.POST, request.FILES)
        #if form.is_valid():
        #cfile=request.FILES['bfile']
          

            # Redirect to the document list after POST
        #     return redirect('my-view')
        # else:
        message = 'The form is not valid. Fix the following error:'
            
        print(title,desc)
        ins = Contact(Title=title,desc=desc)
        ins.save()
        context = {'success': True}
    return render(request,'index.html',context)

def task(request):
    alltasks = Contact.objects.all()
    context = { 'tasks' : alltasks }
    for con in alltasks:
        print(con.Title)
    return render(request,'task.html',context)

