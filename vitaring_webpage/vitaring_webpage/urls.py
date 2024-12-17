# urls.py

from django.urls import path
from django.contrib import admin
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', views.chatbot_response, name='chatbot_response'),  # Zapytania do chatbota
]
