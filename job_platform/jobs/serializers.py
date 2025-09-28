# jobs/serializers.py
from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "title", "description", "location", "employer", "created_at"]
        read_only_fields = ["id", "employer", "created_at"]  # prevent client from sending employer


# from rest_framework import serializers
# from .models import Job

# class JobSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Job
#         #fields = ['id', 'title', 'description', 'location', 'created_at', 'updated_at']
#         fields = "__all__"

#     def create(self, validated_data):
#         user = self.context['request'].user
#         return Job.objects.create(employer=user, **validated_data)
