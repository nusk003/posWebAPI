from rest_framework import serializers

from Employee.models import User

class EmployeeSerializer (serializers.ModelSerializer):

	class Meta:
		model = User
		fields = '__all__'