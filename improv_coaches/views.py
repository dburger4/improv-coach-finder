from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import ImprovCoach
from .serializers import *

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
  my_improv_coaches = ImprovCoach.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'my_improv_coaches': my_improv_coaches
  }
  return HttpResponse(template.render(context, request))


# API View Methods
@api_view(["GET", "POST"])
def api_improv_coaches_list(request):
  if request.method == "GET":
    data = ImprovCoach.objects.all()

    serializer = ImprovCoachSerializer(data, context={"request": request}, many=True)

    return Response(serializer.data)

  elif request.method == "POST":
    serializer = ImprovCoachSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      
      return Response(status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def api_improv_coaches_detail(request, pk):
    try:
        student = ImprovCoach.objects.get(pk=pk)
    except ImprovCoach.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ImprovCoachSerializer(student, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)