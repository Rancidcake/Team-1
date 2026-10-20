"""
Django settings for the Web Security Academy (learning edition).

このサイトは「安全でないコード」をわざと含む学習用教材です。
ローカル(127.0.0.1)でのみ動かすことを前提にしています。
絶対にインターネットへ公開しないでください。
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-learning-only-do-not-deploy")

from dotenv import load_dotenv

# プロジェクト直下の .env を読み込む(GEMINI_API_KEY などを供給する)。
# import だけでは読み込まれないため、必ず呼び出す。.env は .gitignore 済み。
load_dotenv(BASE_DIR / ".env")

DEBUG = os.getenv("DJANGO_DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "securitylabnd",
    ".vercel.app",
    ".vercel.run",
]
if os.getenv("VERCEL_URL"):
    ALLOWED_HOSTS.append(os.getenv("VERCEL_URL"))

CSRF_TRUSTED_ORIGINS = [
    "https://*.vercel.app",
    "https://*.vercel.run",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "labs",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # 注: CsrfViewMiddleware は有効。CSRFラボの「対策前」側は @csrf_exempt で個別に無効化して見せる。
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ラボ用データ置き場（パストラバーサル等で使用）
LAB_DATA_DIR = BASE_DIR / "labs" / "lab_data"
