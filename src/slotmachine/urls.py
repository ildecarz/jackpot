from django.urls import path
from .views import JackPotView

urlpatterns = [
    path('', JackPotView.as_view(), name='jackpot-main'),
    path('<slug:action>/', JackPotView.as_view(), name='jackpot-play'),
]