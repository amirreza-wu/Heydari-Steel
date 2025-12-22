from core.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG",cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast= lambda v: [item.strip() for item in v.split(',')])



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS =  [
    BASE_DIR / 'static'
]


X_FROME_OPTIONS = 'SOMEORIGINE'

CSRF_COOKIE_SECURE=True

AUTH_USER_MODEL = 'accounts.User'


PHONENUMBER_DEFAULT_REGION = 'IR'  # کد کشور پیش‌فرض (ایران در اینجا)
PHONENUMBER_DB_FORMAT = 'NATIONAL'  # فرمت ذخیره در دیتابیس (NATIONAL, E164, INTERNATIONAL)
PHONENUMBER_DEFAULT_FORMAT = 'NATIONAL'  # فرمت پیش‌فرض هنگام نمایش

