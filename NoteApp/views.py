from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
# Create your views here.

from .models import Note
def index(request):
    datas = Note.objects.all()
    context ={
        'datas':datas,
    }
    return render(request, 'index.html',context)

def CreateNote(request):
    if request.method == 'POST':
        heading = request.POST['heading']
        contact = request.POST['contact']
        note = request.POST['note']
        data = Note(heading=heading,contact=contact,note=note)
        data.save()
        messages.success(request,"Note created")


    return render(request,'note/create_note.html')

def MoreInfo(request,id):
    try:
        data = Note.objects.get(id =id)
        if request.method == 'POST':
            if 'submit' in request.POST:
                heading = request.POST['heading']
                contact = request.POST['contact']
                note = request.POST['note']
                data = Note.objects.get(id = id)
                data.heading = heading
                data.contact = contact
                data.note = note
                data.save()
                messages.success(request,"Updated successfully")


    except:
        data =None
        messages.error(request,"Some error occured")
    context = {
        'data': data
    }

    return render(request,'note/more_info.html',context)

def Delete(request,id):
    try:
        data = Note.objects.get(id = id)
        data.delete()
        messages.success(request,"Deleted note: ",data.heading)
    except:
        messages.error(request,"Some error occured")
    return redirect('index')