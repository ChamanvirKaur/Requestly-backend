from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Branch
from .serializers import BranchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    

    def create (self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            {"message" :"Branch Created Successfully", "data" : serializer.data},
            status = status.HTTP_201_CREATED,
            headers=headers 
        )
