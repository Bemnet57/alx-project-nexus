from django.shortcuts import render
from .models import Application
from .permissions import IsApplicant
from rest_framework import viewsets, permissions
from .serializers import ApplicationSerializer
# Create your views here.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.action == "create":
            return [IsApplicant()]   # custom permission
        return [permissions.IsAuthenticated()]
