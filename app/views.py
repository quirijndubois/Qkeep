from django.shortcuts import render
from .models import Note

# Create your views here.
def index(request):
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes': notes})


from django.shortcuts import get_object_or_404, redirect
from .models import Note

def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.content = request.POST.get("content")
        note.title = request.POST.get("title")
        note.save()
        return redirect("index")  # adjust to your main view

def new_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Note.objects.create(title=title, content=content)
        return redirect("index")