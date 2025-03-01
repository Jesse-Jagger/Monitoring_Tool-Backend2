import os
import logging
from celery import Celery
from celery.schedules import crontab

# Set default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server_monitor.settings")

# Create a Celery app instance
app = Celery("server_monitor")

# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in each Django app
app.autodiscover_tasks()

# Logger setup for Celery
logger = logging.getLogger(__name__)

@app.task(bind=True)
def debug_task(self):
    logger.info(f"Debug Task: Request {self.request!r}")
    return f"Debug Task: Request {self.request!r}"

app.conf.beat_schedule = {
    "check_servers_every_minute": {
        "task": "monitoring.tasks.check_server_status",
        "schedule": crontab(minute="*/1"),  # Run every minute
        "args": ("http://10.128.0.2",),  # Replace with real server URL
    },
}
