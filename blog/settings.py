DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'C:/Users/timmi/source/repos/developer-coding-exercise/blog/db.sqlite3',
    }
}

INSTALLED_APPS = [
    "corsheaders",
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
