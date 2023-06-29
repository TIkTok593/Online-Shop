import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
app = Celery('shop')
app.config_from_object('django.conf:settings', namespace='CELERY')  # all celery configuration settings have to start with CELERY as a prefix
app.autodiscover_tasks()  # autodiscover asynchronous tasks for your applications
