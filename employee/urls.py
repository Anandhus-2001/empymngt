from django.urls import path
from employee import views
urlpatterns=[
    path("indexs/",views.LogineView.as_view()),
    path("register",views.RegistrationView.as_view()),
    path("profile/add",views.EmployeeCreateView.as_view(),name="emp-add")


]

