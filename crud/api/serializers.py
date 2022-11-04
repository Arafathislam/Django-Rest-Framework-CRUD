from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        # print(instance.name)
        isntance.name=validated_data.get('name',instance.name)
        # print(instance.name)
        isntance.roll=validated_data.get('roll',instance.roll)
        isntance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
