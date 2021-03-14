from django.urls import path

from .viewsets import ProductorRegistrationAPIView, ProductorRetriveAPIView

urlpatterns = [
	path('test/<int:pk>', ProductorRetriveAPIView.as_view()),
	path('', ProductorRegistrationAPIView.as_view()),
]
