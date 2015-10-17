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

    return render(request,"index.html", {"entries": Entry.objects.all()})
