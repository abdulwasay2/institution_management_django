from rest_framework import serializers

from .models import StudentRollNumberSlip


class StudentRollNumberSlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRollNumberSlip
        fields = "__all__"