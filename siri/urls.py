from django.urls import path

from . import views

app_name = "siri"

urlpatterns = [
    path("", views.index, name="index"),
    path("point/", views.point, name="point"),
    path("create/", views.create, name="create"),
    path("delete/<int:siri_id>", views.delete, name="delete"),
]
