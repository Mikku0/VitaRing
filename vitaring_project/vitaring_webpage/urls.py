# urls.py

from django.urls import path
from django.contrib import admin
from base import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', views.chatbot_response, name='chatbot_response'),  # Zapytania do chatbota
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)