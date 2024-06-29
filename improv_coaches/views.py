from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ImprovCoach

# Create your views here.
def improv_coaches(request):
  all_improv_coaches = ImprovCoach.objects.all().values()
  template = loader.get_template('all_improv_coaches.html')
  context = {
    'all_improv_coaches': all_improv_coaches
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  improv_coach = ImprovCoach.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'improv_coach': improv_coach,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))