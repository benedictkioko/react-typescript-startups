from django.urls import path

from terms import views


app_name = "terms"

urlpatterns = [
    path("", views.TermList.as_view(), name="terms"),
    path("<str:TermId>", views.TermDetailView.as_view(), name="terms-updates"),
]
