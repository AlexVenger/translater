from datetime import datetime
from django.shortcuts import render
from .models import Word

words = [
    {
        "word": "Hello",
        "translations": "Привет",
        "date": datetime.now().strftime("dd-mm-yyyy"),
        "author": "Chungus"
    },
    {
        "word": "World",
        "translations": "Мир",
        "date": datetime.now().strftime("dd-mm-yyyy"),
        "author": "Chungus"
    }
]


def home(request):
    context = {
        "title": "Welcome home!",
        "words": words
    }
    return render(request, "translation_app/home.html", context)
