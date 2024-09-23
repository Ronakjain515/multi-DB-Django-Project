
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from employee.models import Employee
from employee.serializer import ChangeEmployeeSerializer, RetrieveEmployeeSerializer
from utilities import messages
from utilities.utils import ResponseInfo


# Create your views here.
class AddEmployeeAPIView(CreateAPIView):
    """
    Class for creating api for saving new Employee.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = ChangeEmployeeSerializer

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.status_code = status.HTTP_200_OK
        self.response_format = ResponseInfo().response
        super(AddEmployeeAPIView, self).__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        """
        POST Method for saving new Employee.
        """
        employee_serializer = self.get_serializer(data=request.data)
        if employee_serializer.is_valid(raise_exception=True):
            employee_serializer.save()

            self.response_format["data"] = employee_serializer.data
            self.response_format["error"] = None
            self.response_format["status_code"] = self.status_code = status.HTTP_200_OK
            self.response_format["message"] = [messages.CREATION.format("Employee")]
        return Response(self.response_format, status=self.status_code)

class UpdateEmployeeAPIView(UpdateAPIView):
    """
    Class for creating api for updating Employee.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = ChangeEmployeeSerializer

    def __init__(self, **kwargs):
        """
        Constructor function for formatting web response to return.
        """
        self.status_code = status.HTTP_200_OK
        self.response_format = ResponseInfo().response
        super(UpdateEmployeeAPIView, self).__init__(**kwargs)

    def get_queryset(self):
        """
        Method to get queryset for Employee.
        """
        return Employee.objects.get(id=self.kwargs["pk"])

    def patch(self, request, *args, **kwargs):
        """
        PATCH Method for updating Employee.
        """
        try:
            employee = self.get_queryset()
            employee_serializer = self.get_serializer(employee, data=request.data, partial=True)
            if employee_serializer.is_valid(raise_exception=True):
                self.perform_update(employee_serializer)

                self.response_format["data"] = employee_serializer.data
                self.response_format["error"] = None
                self.response_format["status_code"] = status.HTTP_200_OK
                self.response_format["message"] = [messages.UPDATE.format("Employee")]

        except Employee.DoesNotExist:
            self.response_format["data"] = None
            self.response_format["error"] = "Employee"
            self.response_format["status_code"] = status.HTTP_400_BAD_REQUEST
            self.response_format["message"] = [messages.DOES_NOT_EXISTS.format("Employee")]
        return Response(self.response_format, status=self.status_code)


class DeleteEmployeeAPIVIew(DestroyAPIView):
    """
    Class for creating api to delete Employee.
    """
    permission_class = ()
    authentication_classes = ()
    serializer_class = ChangeEmployeeSerializer

    def __init__(self, **kwargs):
        """
        Constructor function for formatting the web response to return.
        """
        self.status_code = status.HTTP_200_OK
        self.response_format = ResponseInfo().response
        super(DeleteEmployeeAPIVIew, self).__init__(**kwargs)

    def get_queryset(self, *args, **kwargs):
        """
        Method to get queryset for Employee.
        """
        return Employee.objects.filter(id=self.kwargs["pk"])


    def delete(self, request, *args, **kwargs):
        """
        DELETE method for deleting Employee.
        """
        try:
            employee = self.get_queryset()
            employee.delete()
            self.response_format["data"] = None
            self.response_format["error"] = None
            self.response_format["status_code"] = status.HTTP_200_OK
            self.response_format["message"] = [messages.DELETION.format("Employee")]


        except Employee.DoesNotExist:
            self.response_format["data"] = None
            self.response_format["error"] = "Category"
            self.response_format["status_code"] = status.HTTP_400_BAD_REQUEST
            self.response_format["message"] = [messages.DOES_NOT_EXISTS.format("Employee")]

        return Response(self.response_format, status=self.status_code)


class GetEmployeeListAPIView(ListAPIView):
    """
    Class for creating api for getting course Category list.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = RetrieveEmployeeSerializer

    def __init__(self, **kwargs):
        """
        Constructor function for formatting the web response to return.
        """
        self.status_code = status.HTTP_200_OK
        self.response_format = ResponseInfo().response
        super(GetEmployeeListAPIView, self).__init__(**kwargs)

    def get_queryset(self):
        """
        Method for getting course Category queryset.
        """
        return Employee.objects.all()

    def get(self, request, *args, **kwargs):
        """
        GET Method for getting course Category list.
        """
        employee_serializer = super().list(request, *args, **kwargs)

        self.response_format["data"] = employee_serializer.data
        self.response_format["error"] = None
        self.response_format["status_code"] = self.status_code = status.HTTP_200_OK
        self.response_format["message"] = [messages.SUCCESS]
        return Response(self.response_format, status=self.status_code)


class GetEmployeeAPIView(RetrieveAPIView):
    """
    Class for creating api for get Employee.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = RetrieveEmployeeSerializer

    def __init__(self, **kwargs):
        """
        Constructor function for formatting web response to return.
        """
        self.status_code = status.HTTP_200_OK
        self.response_format = ResponseInfo().response
        super(GetEmployeeAPIView, self).__init__(**kwargs)

    def get_queryset(self):
        """
        Method to get queryset for Employee.
        """
        return Employee.objects.get(id=self.kwargs["pk"])

    def get(self, request, *args, **kwargs):
        """
        PATCH Method for updating Employee.
        """
        try:
            employee = self.get_queryset()
            employee_serializer = self.get_serializer(employee, many=False)

            self.response_format["data"] = employee_serializer.data
            self.response_format["error"] = None
            self.response_format["status_code"] = status.HTTP_200_OK
            self.response_format["message"] = [messages.UPDATE.format("Employee")]

        except Employee.DoesNotExist:
            self.response_format["data"] = None
            self.response_format["error"] = "Employee"
            self.response_format["status_code"] = status.HTTP_400_BAD_REQUEST
            self.response_format["message"] = [messages.DOES_NOT_EXISTS.format("Employee")]
        return Response(self.response_format, status=self.status_code)

