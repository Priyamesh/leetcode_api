from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


# Create your views here.


@api_view(["GET"])
def api_list(request):
    api_urls = {"ye pe ye": "yeeee"}
    return Response(api_urls)


@api_view(["GET"])
def ques_list(request):
    ques = Questions.objects.all()
    serializer = QuesSerializers(ques, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def quesDetail(request, pk):
    ques = Questions.objects.get(id=pk)
    serializer = QuesSerializers(ques, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def quesCreate(request):
    serializer = QuesSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
