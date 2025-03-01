from rest_framework import serializers
from .models import Server, ServerStatusHistory, AlertLog

class ServerSerializer(serializers.ModelSerializer):
    last_checked = serializers.ReadOnlyField()
    last_online = serializers.ReadOnlyField()
    next_check_time = serializers.ReadOnlyField()
    
    class Meta:
        model = Server
        fields = '__all__'
        read_only_fields = ['last_checked', 'last_online', 'next_check_time']

    def validate_url(self, value):
        """Ensures the URL starts with http or https"""
        if not value.startswith(('http://', 'https://')):
            raise serializers.ValidationError("URL must start with http:// or https://")
        return value

    def validate_timeout(self, value):
        """Ensures timeout is within a reasonable range"""
        if value < 1 or value > 60:
            raise serializers.ValidationError("Timeout must be between 1 and 60 seconds.")
        return value

    def validate_check_frequency(self, value):
        """Ensures that the check frequency is reasonable"""
        if value < 60 or value > 86400:  # Min 1 min, Max 24 hours
            raise serializers.ValidationError("Check frequency must be between 60 and 86400 seconds.")
        return value


class ServerStatusHistorySerializer(serializers.ModelSerializer):
    checked_at = serializers.ReadOnlyField()
    
    class Meta:
        model = ServerStatusHistory
        fields = '__all__'
        read_only_fields = ['checked_at']


class AlertLogSerializer(serializers.ModelSerializer):
    sent_at = serializers.ReadOnlyField()
    
    class Meta:
        model = AlertLog
        fields = '__all__'
        read_only_fields = ['sent_at']
