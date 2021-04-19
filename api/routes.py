from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

routers = DefaultRouter()

urlpatterns = [
    path("orgs/", views.OrganizationList.as_view()),
    path('orgs/<str:pk>/', views.OrganizationDetail.as_view())
]
