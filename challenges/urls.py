from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,  name="index"),
    path("<int:month>", views.monthlyChallangeByNumber),
    path("<str:month>", views.monthlyChange, name="month-challenge"),
]
