from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# --- Базовая директория проекта ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Безопасность ---
DEBUG = os.getenv("DEBUG", "False") == "True"

SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key")

ALLOWED_HOSTS = ["*", ".onrender.com"]

# --- Приложения ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index',
]

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- Основные настройки ---
ROOT_URLCONF = 'meros.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Если позже добавим templates вне приложений — пропишем сюда
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meros.wsgi.application'

# --- База данных ---
DATABASES = {
    'default':
        dj_database_url.config(default=os.getenv("DATABASE_URL"))
}

# --- Валидация пароля ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Язык и время ---
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# --- ⚙️ Статические и медиа файлы ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MIDDLEWARE.insert(1, "whitemoise.middleware.WhiteNoiseMiddleware")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# 📂 Где хранятся твои CSS, JS, картинки проекта
STATICFILES_DIRS = [
    BASE_DIR / "index" / "static",
]

# 🖼 Фото учителей и другие загружаемые файлы
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# --- ID по умолчанию ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
