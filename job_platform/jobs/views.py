# jobs/views.py
from rest_framework import viewsets, permissions
from .models import Job
from .serializers import JobSerializer
from .permissions import IsEmployer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsEmployer()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)


# from django.shortcuts import render
# from rest_framework import filters

# # Create your views here.
# from rest_framework import viewsets, permissions
# from .models import Job
# from .serializers import JobSerializer
# from .permissions import IsEmployer  # custom permission

# class JobViewSet(viewsets.ModelViewSet):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ["title", "category","description", "location"] #enables ?search=...
#     oredering_fields = ["created_at", "title"]

#     def get_permissions(self):
#         if self.action in ['create', 'update', 'partial_update', 'destroy']:
#             return [IsEmployer()]
#         return [permissions.AllowAny()]
    
#     def perform_create(self, serializer):
#         serializer.save(employer=self.request.user)

