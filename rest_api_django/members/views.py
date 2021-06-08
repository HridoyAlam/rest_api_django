from django.shortcuts import render
from rest_framework import viewsets
from .models import Member
from .serializer import MemberSerializer

class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# Create your views here.
