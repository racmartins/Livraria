import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# Security and Debug Settings
# ----------------------------

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!m#gfom8_#r@@1($^t9d(oroej&ew(i#3lz6ecq0h0@$)oehj%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Hosts allowed to access the application (empty for development)
ALLOWED_HOSTS = []

# ----------------------------
# Application Definition
# ----------------------------

INSTALLED_APPS = [
    # Django core apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Custom apps
    "livros",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# ----------------------------
# Templates Configuration
# ----------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],  # Templates directory
        "APP_DIRS": True,  # Search for templates in installed apps
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ----------------------------
# Database Configuration
# ----------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # SQLite database
        "NAME": BASE_DIR / "db.sqlite3",  # Database file path
    }
}

# ----------------------------
# Password Validation
# ----------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ----------------------------
# Internationalization
# ----------------------------

LANGUAGE_CODE = "pt-pt"  # Portuguese (Portugal) language
TIME_ZONE = "UTC"  # Coordinated Universal Time
USE_I18N = True  # Enable internationalization
USE_TZ = True  # Use timezone-aware datetimes

# ----------------------------
# Static Files (CSS, JavaScript, Images)
# ----------------------------

STATIC_URL = "/static/"  # URL prefix for static files
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Directory for static files
]

# ----------------------------
# Default Primary Key Field
# ----------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------------
# Authentication Redirects
# ----------------------------

LOGIN_REDIRECT_URL = "/"  # Redirect after login
LOGOUT_REDIRECT_URL = "/"  # Redirect after logout
