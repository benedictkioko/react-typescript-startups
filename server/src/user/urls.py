from django.urls import path

from user import views


app_name = "auth"

urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="create"),
    path("login/", views.CreateTokenView.as_view(), name="token"),
    path("profile/", views.ManageUserView.as_view(), name="profile"),
]
