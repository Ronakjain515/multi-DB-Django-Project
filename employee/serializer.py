from rest_framework import serializers

from employee.models import Employee


class ChangeEmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer class for adding and updating course category.
    """
    class Meta:
        model = Employee
        fields = ("name", "phone", "email")


class RetrieveEmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer class for getting course category.
    """
    class Meta:
        model = Employee
        fields = ("id", "name", "phone", "email")

