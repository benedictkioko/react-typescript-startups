from django.urls import path

from scores import views


app_name = "scores"

urlpatterns = [
    path("", views.ScoreList.as_view(), name="scores"),
    path("<str:ScoreId>", views.ScoreDetailView.as_view(), name="scores-updates"),
]
