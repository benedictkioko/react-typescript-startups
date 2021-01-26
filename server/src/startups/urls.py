from django.urls import path

from startups import views


app_name = "students"

urlpatterns = [
    path("", views.StudentsList.as_view(), name="students"),
    path(
        "<str:StudentId>", views.StudentsDetailView.as_view(), name="students-updates"
    ),
]
