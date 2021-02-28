from rest_framework import serializers

from .models import HocTap

class HoctapSerializer(serializers.ModelSerializer):

    class Meta:
        model = HocTap
        #fields = ('MSSV','HOTEN','LOP','SDT','note')
        fields = '__all__'
