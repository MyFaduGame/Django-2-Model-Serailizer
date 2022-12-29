from django.shortcuts import render
from User.serializers import SampleSerializer
from User.models import user
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class sampleview(APIView):
    def get(self,request):
        qs = user.objects.all()
        serializer = SampleSerializer(qs,many=True)

        return Response(serializer.data)

    def post(self,request):
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

