from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProjectSerializer
from .models import Project

# Create your views here.


class ProjectView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Project.objects.all()
        serializer = ProjectSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
