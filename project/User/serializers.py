from rest_framework import serializers
from User.models import user,email

class EamilSerializer(serializers.ModelSerializer):
    class Meta:
        model = email
        fields = "__all__"

class SampleSerializer(serializers.ModelSerializer):
    email = EamilSerializer(many=True)
    class Meta:
        model = user
        fields = "__all__"
        depth = 1
        

