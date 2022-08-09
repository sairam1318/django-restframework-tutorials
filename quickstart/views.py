from rest_framework import viewsets, status, request, filters, generics, pagination
from rest_framework.response import Response

from .models import *
from .serializers import *


# Create your views here.


# to fetch all records:
# class UsersViewSet(viewsets.ModelViewSet):
#       queryset = Users.objects.filter()
#       serializer_class = UsersSerializer
#
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.filter()
    serializer_class = UsersSerializer
    filterset_fields = ["userid"]

    def create(self, request):
        payload = request.data
        queryset = Users.objects.filter(pk=payload["userid"]).first()
        instance = None
        if queryset is not None:
            instance = UsersSerializer(queryset, data=payload, partial=True)
        else:
            instance = UsersSerializer(data=payload)
        if not instance.is_valid():
            errors = instance.errors
            return Response(errors)
        instance.save()
        return Response(instance.data)


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = Userrole.objects.filter()
    serializer_class = UserRoleSerializer
    filterset_fields = ["id"]


class StudentsViewSet(viewsets.ModelViewSet):
    # queryset = Students.objects.filter(**{'student_id': 1})
    queryset = Students.objects.filter()
    serializer_class = StudentsSerializer
    filterset_fields = ["student_id"]


class CustomerViewSet(viewsets.ModelViewSet):
    # queryset = Students.objects.filter(**{'student_id': 1})
    queryset = Customer.objects.filter()
    serializer_class = CustomerSerializer
    filterset_fields = ["customer_id"]
