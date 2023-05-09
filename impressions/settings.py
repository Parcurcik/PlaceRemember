import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-)jguq_%lu=28sn_yn%#38t2#0#4ci9f#h4-#n7a#wjk&=h)_wm'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'memories',
    'social_django',
]
AUTHENTICATION_BACKENDS = [
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1078716205901-6dpr67ckk2r70dto88q7e4cl5j63dd3v.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_VK_OAUTH2_KEY = '51639630'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'nzZL6MDf36V3yqPmzGG8'

SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_LOGIN_REDIRECT_URL = '/google_callback'
SOCIAL_AUTH_VK_OAUTH2_LOGIN_REDIRECT_URL = '/vk_callback'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'authorization.middleware.AuthRequiredMiddleware'
]

ROOT_URLCONF = 'impressions.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',

            ],
        },
    },
]

WSGI_APPLICATION = 'impressions.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
