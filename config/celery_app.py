import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
if not ("DJANGO_SETTINGS_MODULE" in os.environ):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

from configurations import importer
importer.install()

app = Celery("Expertonica-test")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
        # Executes everyday at 6:00
            'add-at-6-everyday': {
            'task': 'live_probes.tasks.take_live_probes',
            'schedule': crontab(hour="6"),
        }
    }
