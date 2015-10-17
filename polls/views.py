
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from .models import Entry
from django.shortcuts import render, redirect

def hallo(request):#



    if request.method == "POST":
        entry_id = request.POST.get("entry")
        entry = Entry.objects.get(id=entry_id )
        if "up" in request.POST:
            entry.upvotes = entry.upvotes +1
        elif "down" in request.POST:
            entry.downvotes = entry.downvotes +1

        entry.save()
        return redirect("/hallo#entry-" + str(entry.id))







    hauptseite = requests.get("http://www.bundestag.de/tagesordnung")
    soup = BeautifulSoup(hauptseite.text, 'html.parser')
    verlinkung = soup.select("div.linkIntern a")[0]
    verlinkung["href"]











    urle = "http://www.bundestag.de" + verlinkung["href"]
    response = requests.get(urle)

    #file = open("C:\Users\Tadeo\mysite\\bundestag.txt","r").read().decode("utf-8")
    soup = BeautifulSoup(response.text, 'html.parser')

    inhalt = soup.select("div.inhalt")[0]

    hlist = (inhalt.select("h4"))
    plist = (inhalt.select("p"))
    hplist = []
    for i in range(0,len(hlist),1):
        hplist.append([hlist[i],plist[i*2]])






    h1 = soup.select("div.inhalt h1")[0]
    time = h1.text.split(",")[2].strip()
    timeformated = datetime.strptime(time, "%d.%m.%Y")



    for hpelem in hplist:
        Entry.objects.get_or_create(sitzung=urle,
        tpunkt=hpelem[0].text,
        defaults={"text": hpelem[1].text, "datum": timeformated})






    return render(request,"index.html", {"entries": Entry.objects.all()})
