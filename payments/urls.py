from django.urls import path

from .views import PaymentView,GatewayView


urlpatterns = [
    path('payments/', PaymentView.as_view(), name='Payment-list'),
    path('gateways/', GatewayView.as_view(), name='Gateway-list'),
]