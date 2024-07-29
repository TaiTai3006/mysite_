from django.urls import path
from qlnv.views import *

urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("salaryCalculation/", salaryCalculation, name="salaryCalculation"),
    path("update/<id>/", update, name="update"),
    path("delete/<id>/", delete, name="delete"),
    path("getNhanVienInfo/<id>/", getNhanVienInfo, name="getNhanVienInfo"),
]
