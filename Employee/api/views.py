from rest_framework.generics import ListAPIView
from Employee.models import User
from .serializers import EmployeeSerializer
from rest_framework.permissions import BasePermission

class IsSuperAdmin (BasePermission):

	message = "User must be a super Admin"

	def has_permission(self,request,view):

		try:
			return request.user.userType.pk == 1
		except:
			return False
 
class EmployeeListView (ListAPIView):

	queryset =  User.objects.all()
	serializer_class = EmployeeSerializer
	permission_classes = (IsSuperAdmin,)