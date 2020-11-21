from django.shortcuts import render
import requests
from django.core.mail import send_mail
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Task
from django.http import HttpResponseRedirect
#from . import meera


def index(request):
    return render(request,"index.html") #{"response" : meera.get_reply(inp)})

#testimonial
def profile(request):
    tasks=Task.objects.all().order_by("date")
    return render(request,"profile.html",{
        "tasks":tasks
    })

@csrf_exempt
def add_todo(request):
    added_date=timezone.now()
    content=request.POST['task'] #task is name of the form
    created_object=Task.objects.create(date=added_date, task=content)
    return HttpResponseRedirect("/profile")

@csrf_exempt
def delete_todo(request , todo_id):
    Task.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/profile")

#help
def base(request):
    url="https://www.narayanahealth.org/hospitals/specialities/breast-cancer"
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.findAll("div",{"class":"view view-hospitals-all-view view-id-hospitals_all_view view-display-id-page search-content view-dom-id-0e815c983b5fd506430858b308f14dd7"})
    final_postings = []
    images = ["https://www.narayanahealth.org/sites/default/files/hospitals/nh-clinic-jayanagar.jpg",
              "https://www.narayanahealth.org/sites/default/files/hospitals/mazumdar-shaw-medical-centre.jpg",
              "https://www.narayanahealth.org/sites/default/files/hospitals/nmh-ahmedabad.jpg",
              "https://www.narayanahealth.org/sites/default/files/hospitals/dnsh-delhi.jpg",
              "https://www.narayanahealth.org/sites/default/files/hospitals/nsh-howrah.jpg",
              "https://www.narayanahealth.org/sites/default/files/hospitals/nmh-mysore.jpg"]

    maps = ["https://www.google.com/maps/place/Narayana+Multispeciality+Clinic,+Jayanagar/@12.9289017,77.5804002,16.75z/data=!4m5!3m4!1s0x0:0xdcde9737879da581!8m2!3d12.9291114!4d77.5827269?hl=en",
            "https://www.google.com/maps/place/Mazumdar+Shaw+Medical+Center/@12.8069375,77.6926651,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x51693da9325cf807!8m2!3d12.8069375!4d77.6948538?hl=en",
            "https://www.google.com/maps/place/Narayana+Multispeciality+Hospital/@23.0226551,72.6214628,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x333a7f0f520404a7!8m2!3d23.0226551!4d72.6236515?hl=en",
            "https://www.google.com/maps/place/Dharamshila+Narayana+Superspeciality+Hospital/@28.6025216,77.3119395,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x75d3303be5f4d44d!8m2!3d28.6025216!4d77.3141282?hl=en",
            "https://www.google.com/maps/place/Narayana+Superspeciality+Hospital,+Howrah/@22.5626471,88.3057444,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x4e6e77463ab93f24!8m2!3d22.5626471!4d88.3079331?hl=en",
            "https://www.google.com/maps/place/Narayana+Multispeciality+Hospital/@12.3452406,76.6708521,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0xfa137a5dcf03a77b!8m2!3d12.3452406!4d76.6730408?hl=en"]

    name = ["Narayana multispeciality clinic, jayanagar" ,
            "Mazumdar shaw medical center, bommasandra",
            "Narayana multispeciality hospital, ahmedabad",
            "Dharamshila narayana superspeciality hospital",
            "Narayana superspeciality hospital, howrah",
            "Narayana multispeciality hospital, mysore"]



    doc_info = ["No.108, Uday House, 30th Cross, 8th B Main Road, 4th Block, Jayanagar,Bangalore,  Karnataka  - 560011",
                "258/A, Bommasandra Industrial Area, Hosur Road, Anekal Taluk, Bangalore,  Karnataka  - 560099",
                "Nr. Chakudiya Mahadev, Rakhial Cross Road, Opp. Rakhial Police Station, Rakhial, Ahmedabad,  Gujarat  - 380023",
                "Vasundhara Enclave, Near New Ashok Nagar Metro Station, Dallupura, New Delhi,  Delhi  - 110096",
                "120/1, Andul Rd, Near Nabanna, Howrah,  West Bengal  - 711103",
                "CAH/1, 3rd Phase, Devanur 2nd Stage, R.S.Naidu Nagar, Mysore,  Karnataka  - 570019"]
    for i in range (6):
        final_postings.append((images[i], name[i], doc_info[i], maps[i] ))
    return render(request, "base.html",{
        'final_postings' : final_postings
        })

