#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# 🔥 Загружаем Django перед работой с моделями
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Eleganza.settings')  # ✅ Загружаем настройки Django

django.setup()  # ✅ Загружаем Django, чтобы модели работали

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

def generate_token(username):
    """Генерирует Refresh и Access токен для указанного пользователя."""
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        refresh = RefreshToken.for_user(user)
        print(f"Refresh Token: {refresh}")
        print(f"Access Token: {refresh.access_token}")
    except User.DoesNotExist:
        print(f"Ошибка: Пользователь '{username}' не найден.")

def main():
    """Run administrative tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if len(sys.argv) > 1 and sys.argv[1] == "generate_token":
        if len(sys.argv) > 2:
            generate_token(sys.argv[2])
        else:
            print("Ошибка: Укажите имя пользователя. Например:")
            print("python manage.py generate_token your_username")
    else:
        execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
