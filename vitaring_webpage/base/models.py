from django.db import models


class KnowledgeBase(models.Model):
    # Kategoria (np. "smartwatch", "bateria", "system operacyjny")
    category = models.CharField(max_length=100)
    # Treść wiedzy, np. definicje, porady, informacje ogólne
    content = models.TextField()

    def __str__(self):
        return f"{self.category}: {self.content[:50]}"  # Wyświetl pierwsze 50 znaków treści
