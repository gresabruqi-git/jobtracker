from django.urls import path

from .views import (
    JobApplicationListCreateView,
    JobApplicationRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', JobApplicationListCreateView.as_view(), name='application-list'),
    path('<int:pk>/', JobApplicationRetrieveUpdateDestroyView.as_view(), name='application-detail'),
]
