from pyexpat import model
from django.urls import clear_script_prefix
from rest_framework import serializers
from .models import *


class QuesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"
