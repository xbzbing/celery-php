BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "gdr"
BROKER_PASSWORD = "test"
BROKER_VHOST = "wutka"

CELERY_RESULT_BACKEND = "amqp"

CELERY_IMPORTS = ("tasks", )

CELERY_RESULT_SERIALIZER = "json"
