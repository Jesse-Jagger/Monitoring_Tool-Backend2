from django.db import models
from django.utils.timezone import now

class Server(models.Model):
    STATUS_CHOICES = [
        ("online", "Online"),
        ("offline", "Offline"),
        ("unknown", "Unknown"),
    ]

    name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="unknown")
    last_checked = models.DateTimeField(auto_now=True)
    last_online = models.DateTimeField(null=True, blank=True)
    response_time = models.FloatField(null=True, blank=True)
    timeout = models.IntegerField(default=5)  # Timeout in seconds
    check_frequency = models.IntegerField(default=300)  # Monitoring interval in seconds
    next_check_time = models.DateTimeField(default=now)
    alert_email = models.EmailField(null=True, blank=True)
    alert_webhook = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.status})"


class ServerStatusHistory(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="history")
    status = models.CharField(max_length=10, choices=Server.STATUS_CHOICES)
    response_time = models.FloatField(null=True, blank=True)
    http_status_code = models.IntegerField(null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)
    checked_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.server.name} - {self.status} ({self.checked_at})"


class AlertLog(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="alerts")
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.server.name} at {self.sent_at}"
