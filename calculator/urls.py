from django.urls import path
from calculator import views
urlpatterns=[
    path("home",views.HomeView.as_view(),name="calc-home"),
    path("add",views.AddView.as_view(),name="calc-add"),
    path("sub",views.SubView.as_view(),name="calc-sub"),
    path("mul",views.MulView.as_view(),name="calc-mul"),
    path("div",views.DivView.as_view(),name="calc-div"),
    path("mod",views.ModView.as_view(),name="calc-mod"),
    path("fact",views.FactView.as_view(),name="calc-fact"),
    path("exp",views.ExpView.as_view(),name="calc-exp"),
    path("wordcount",views.WordCountView.as_view(),name="calc-wordcount"),
  #  path("prime",views.PrimeView.as_view()),

]