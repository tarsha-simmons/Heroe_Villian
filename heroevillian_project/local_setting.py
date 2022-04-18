# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=nm*xapgi#g1ajhnrwu$ok6bkviwb764+-iadrfy)-37u8@%+r'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroesvillians_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
