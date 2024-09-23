from django.conf import settings
print(settings.TIME_ZONE)
db_1 = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "dynamic_db_org_1",
        'USER': "postgres",
        'PASSWORD': "root",
        'PORT': "5432",
        'HOST': "localhost"

    }
db_2 = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "dynamic_db_org_2",
        'USER': "postgres",
        'PASSWORD': "root",
        'PORT': "5432",
        'HOST': "localhost"

}