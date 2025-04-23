from django.urls import path
from locations import views

urlpatterns = [
    path('locations/', views.LocationList.as_view()),
    path('locations/<slug:slug>/', views.LocationDetail.as_view()),
    path('locations/<slug:slug>/posts/', views.LocationPostList.as_view()),
    path('locations/popular/', views.TopLocationList.as_view()),
]
