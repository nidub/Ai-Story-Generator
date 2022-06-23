from django.http import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import GetText,Stories_Submitted
from . import Project
# Create your views here.


def index(response):
    return render(response, "main/base.html", {})

def entries_view(response):
    form=GetText()
    return render(response, "main/entries.html", {'form':form})

def story_view(response):
    True_or_False=False
    if response.method == "POST":
        #print(1)
        form=Stories_Submitted(response.POST)
        #print(form)
        if form.is_valid():
            e=form.cleaned_data["my_story"]
            stories_written=stories(story=e)
            stories_written.save()
            True_or_False=True
    else:
        form=Stories_Submitted()
    return render(response, "main/stories.html", {'form':form, 'submitted':True_or_False})

def generated_view(response):
    if response.method == "POST":
        #print(1)
        form=GetText(response.POST)
        #print(form)
        if form.is_valid():
            e=form.cleaned_data["given_text"]
            g=form.cleaned_data["g_Choice"]
            t=entries(entry=e)
            t.save()
    else:
        form=GetText()

    #print(e,g)

    #print(Project.func(e,g))
    generated_info=Project.func(e,g)
    tosave=generated(generated_text=generated_info)
    tosave.save()
    return render(response, "main/generated.html", {'form':form, 'generated':generated_info})

def storiesDatabase(response):
    get_Stories=stories.objects.all()

    return render(response,"main/storiesDatabase.html",{'get_Stories':get_Stories})

def generatedHistory(response):
    generated_Hist=generated.objects.all()

    return render(response,"main/generatedHistory.html",{'generated_Hist':generated_Hist})