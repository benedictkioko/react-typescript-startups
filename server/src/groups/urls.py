from django.urls import path

from groups import views


app_name = "groups"

urlpatterns = [
    path("", views.GroupList.as_view(), name="groups"),
    path("<str:GroupId>", views.GroupDetailView.as_view(), name="groups-updates"),
]
