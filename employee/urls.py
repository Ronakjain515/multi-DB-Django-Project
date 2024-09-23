from django.urls import path

from .views import (
    AddEmployeeAPIView, UpdateEmployeeAPIView, DeleteEmployeeAPIVIew, GetEmployeeListAPIView, GetEmployeeAPIView,
)


urlpatterns = [
    path("addEmployee", AddEmployeeAPIView.as_view(), name="add-employee"),
    path("updateEmployee/<int:pk>", UpdateEmployeeAPIView.as_view(), name="update-employee"),
    path("deleteEmployee/<int:pk>", DeleteEmployeeAPIVIew.as_view(), name="delete-employee"),
    path("getEmployeeList", GetEmployeeListAPIView.as_view(), name="get-employee-list"),
    path("getEmployee/<int:pk>", GetEmployeeAPIView.as_view(), name="get-employee"),

]
