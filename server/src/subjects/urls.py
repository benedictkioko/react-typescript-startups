from django.urls import path

from subjects import views


app_name = "subjects"

urlpatterns = [
    path("", views.SubjectList.as_view(), name="subjects"),
    path(
        "<str:SubjectId>",
        views.SubjectDetailView.as_view(),
        name="subjects-updates",
    ),
]
