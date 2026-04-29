from .base import *
DATABASES={"default":{"ENGINE":"django.db.backends.postgresql","NAME":os.getenv("POSTGRES_DB","gestion_ecole"),"USER":os.getenv("POSTGRES_USER","postgres"),"PASSWORD":os.getenv("POSTGRES_PASSWORD","postgres"),"HOST":os.getenv("POSTGRES_HOST","localhost"),"PORT":os.getenv("POSTGRES_PORT","5432")}}
SECURE_PROXY_SSL_HEADER=("HTTP_X_FORWARDED_PROTO","https")
