from celery import shared_task
import requests
import logging
from django.utils.timezone import now
from .models import Server, ServerStatusHistory, AlertLog
from django.core.mail import send_mail
from django.conf import settings

#logging setup
logger = logging.getLogger(__name__)

@shared_task(bind=True, autoretry_for=(requests.RequestException,), retry_kwargs={'max_retries': 3, 'countdown': 10})
def check_server_status(self, server_id):
    """
    Task to check the status of a server and update database records.
    Sends an email alert if the server is down.
    """
    try:
        server = Server.objects.get(id=server_id)  # Fetches the server by its ID
        response = requests.get(server.url, timeout=5)
        status = "UP" if response.status_code == 200 else "DOWN"
    except (requests.RequestException, Server.DoesNotExist) as e:
        status = "DOWN"
        logger.error(f"Error checking {server.url if 'server' in locals() else 'Unknown Server'}: {str(e)}")

    # Update server status history
    ServerStatus.objects.create(server=server, status=status, checked_at=now())

    # If status is DOWN, create an alert log and send email
    if status == "DOWN":
        AlertLog.objects.create(server=server, alert_message=f"Server {server.name} is down!")

        # Send email alert
        send_mail(
            subject=f"Alert: {server.name} is DOWN!",
            message=f"The server {server.name} ({server.url}) is not responding.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],  # Ensure ADMIN_EMAIL is in settings.py
        )
    
    logger.info(f"Checked {server.url}: {status}")
    return f"Checked {server.url}: {status}"

@shared_task
def check_all_servers():
    """Task to check all registered servers."""
    servers = Server.objects.all()
    for server in servers:
        check_server_status.delay(server.id)  # Asynchronous task execution
    return f"Triggered checks for {servers.count()} servers."
