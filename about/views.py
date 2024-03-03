from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
  about = About.objects.all().order_by('-updated_on').first()
  collaborate_form = CollaborateForm()

  if request.method == "POST":
    collaborate_form = CollaborateForm(data=request.POST)
    if collaborate_form.is_valid:
      collaborate_form.save()
      messages.add_message(
        request, messages.SUCCESS,
        'Collaboration request received. It may take up to 2 working days for a response.'
      )


  return render(
    request,
    "about/about.html",
    {
      "about": about,
      "collaborate_form": collaborate_form,
    },
  )