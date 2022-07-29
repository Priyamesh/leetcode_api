from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def loginpage(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", context)

    return render(request, "login.html", context)


@login_required
def home(request):
    return render(request, "index.html", {})


def logoutpage(request):
    logout(request)
    return redirect("home")


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
    serializer = QuesSerializersGET(ques, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def quesDetail(request, pk):
    ques = Questions.objects.get(id=pk)
    serializer = QuesSerializersGET(ques, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def quesCreate(request):
    print(request.data)
    print("entered in create view")
    serializer = QuesSerializersPOST(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        print("rwergiunb")
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def quesUpdate(request, pk):
    ques = Questions.objects.get(id=pk)
    print(ques.revision_count)
    serializer = QuesSerializersPOST(instance=ques, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
