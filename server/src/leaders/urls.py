from django.urls import path

from leaders import views


app_name = "leaders"

urlpatterns = [
    path("", views.LeaderList.as_view(), name="leaders"),
    path("<str:LeaderId>", views.LeaderDetailView.as_view(), name="leaders-updates"),
]