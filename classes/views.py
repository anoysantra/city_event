from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Classes,Section
from .forms import ClassForm,SectionForm,SectionSearch
# Create your views here.

def AddClasses(request):
    classes=Classes.objects.all()
    if request.method=='POST':
        form=ClassForm(request.POST)
        print(request.POST)

        if form.is_valid():
            class_check=form.cleaned_data['class_name']


            for e in classes:
                if class_check == e.class_name:
                    return HttpResponse("Class Already Present. Error")

            print("Class form is valid")
            form.save()
            return redirect('class_list')
    else:
        form= ClassForm()  

    return render(request, 'class_add.html', {'form':form})  


def ListClasses(request):

    classes = Classes.objects.all()
    print(classes)
    return render(request, 'class_list.html',{'classes': classes})


def DeleteClasses(request,class_name):

    #class_obj = get_object_or_404(Classes, class_name=class_name) 
    class_obj = Classes.objects.filter(class_name=class_name)
    print(class_obj)
    
    if request.method == 'POST':
        class_obj.delete()
        return redirect('class_list')
    
    return render(request, 'class_delete.html', {'class_obj': class_obj})


def UpdateClasses(request,class_name):
    instance = get_object_or_404(Classes, class_name=class_name)
    print(instance)
    classes=Classes.objects.all()

    if request.method == 'POST':
        form = ClassForm(request.POST, instance=instance)
        print("New Data : ", request.POST )
        if form.is_valid():               
                class_check=form.cleaned_data['class_name']
                for e in classes:
                    if class_check == e.class_name:
                        return HttpResponse("Class Already Present.Cannot be updated Error")
                form.save()
                return redirect('class_list')
    else:
        form = ClassForm(instance=instance)

    return render(request, 'class_update.html', {'form': form, 'instance': instance})



def SectionAdd(request,class_name):
    classes = Classes.objects.get(class_name=class_name)
    sections=Section.objects.all()  #debug
    print(sections)  

    print("Class is:",classes)
    
    if request.method=='POST':
        print(request.POST)
        form=SectionForm(request.POST)
        
        if form.is_valid():
            section_check=form.cleaned_data['section_name'] #debug
            print(section_check)

            for e in sections:
                if section_check == e.section_name:
                    return HttpResponse("Section Already Present. Error")
            
            print(type(section_check))
            print("Its valid")
            form.instance.class_name = classes
            form.save()
            return redirect('class_list')
        
    else:
        print("Not Valid")
        form=SectionForm()

    return render(request,'section_add.html',{'classes':classes , 'form':form})

def SectionList(request,class_name):
    classes=get_object_or_404(Classes,class_name=class_name)
    section=Section.objects.filter(class_name=classes).values()
    print("Event is: ",section)
    return render(request, 'section_list.html', {'classes': classes, 'section': section})

def SectionDelete(request,class_name,section_name):
    classes=get_object_or_404(Classes,class_name=class_name)
    section=get_object_or_404(Section, class_name=classes, section_name=section_name)
    #section=Section.objects.filter(class_name=classes, section_name=section_name)
    if request.method == 'POST':
        section.delete()
        return redirect('class_list')
    
    return render(request, 'section_delete.html', {'classes':classes, 'section':section})

def SectionUpdate(request,class_name,section_name):
    classes=get_object_or_404(Classes,class_name=class_name)
    section=get_object_or_404(Section, class_name=classes, section_name=section_name)

    if request.method=='POST':
        form=SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('class_list')
        
    else:
        form=SectionForm()

    return render(request, 'section_update.html', {'form': form, 'classes': classes, 'section':section})


def SearchClassToSeeSection(request):
    try:
        if request.method=='POST':
            form=SectionSearch(request.POST)
            if form.is_valid():
                class_name=form.cleaned_data['class_name']
                url="{}".format(class_name)
                return HttpResponseRedirect(url)
        else:
            form=SectionSearch()

    except Exception as e:
        return HttpResponse(f"<h1> The class you are trying to search is not found.The error is:{e}!!</h1>")
    
    return render(request,'section_search.html',{'form':form})



