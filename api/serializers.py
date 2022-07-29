from pyexpat import model
from django.urls import clear_script_prefix
from rest_framework import serializers
from .models import *


class QuesSerializersGET(serializers.ModelSerializer):
    date_solved = serializers.DateTimeField(format="%d-%b-%y")
    date_revised = serializers.DateTimeField(format="%d-%b-%y")

    # print("fegrnkjfnkn")

    class Meta:
        model = Questions
        fields = "__all__"


class QuesSerializersPOST(serializers.ModelSerializer):
    # date_solved = serializers.DateTimeField(format="%d-%b-%y")
    # date_revised = serializers.DateTimeField(format="%d-%b-%y")

    # print("fegrnkjfnkn")

    class Meta:
        model = Questions
        fields = "__all__"
