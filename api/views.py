from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


# Create your views here.


def home(request):
    return render(request, "index.html", {})


@api_view(["GET"])
def api_endpoints(request):
    api_urls = {
        "api/": "api endpoints",
        "api/ques": "list of all questions",
        "api/ques/<pk>": "deatils abot the ques",
        "api/create": "create a ques entry",
    }
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
    print(request.data)
    print("entered in create view")
    serializer = QuesSerializers(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        print("rwergiunb")
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def quesUpdate(request, pk):
    ques = Questions.objects.get(id=pk)
    print(ques.revision_count)
    serializer = QuesSerializers(instance=ques, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
