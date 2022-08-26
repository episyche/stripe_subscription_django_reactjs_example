from subscription import views
from django.urls import path
from .views import*

urlpatterns = [
    path('create-subscription/' , CreateSubscription.as_view()),
    path('webhook-test/' , WebHook.as_view()) , 
]