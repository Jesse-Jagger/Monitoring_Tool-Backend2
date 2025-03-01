from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Server, ServerStatusHistory, AlertLog
from .serializers import ServerSerializer, ServerStatusHistorySerializer, AlertLogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse


@api_view(['GET'])
def api_root(request):
    """Root API view for the monitoring app."""
    return Response({
        'servers': request.build_absolute_uri('servers/'),
        'server-detail': request.build_absolute_uri(reverse('server-detail', args=[1])),
        'server-status-history': request.build_absolute_uri(reverse('server-status-history', args=[1])),
        'server-alerts': request.build_absolute_uri(reverse('server-alerts', args=[1])),
    })

class ServerListCreateView(generics.ListCreateAPIView):
    """
    API View to list and create servers.
    - This Requires authentication.
    - Supports filtering by name, status, and IP address.
    - Implements pagination and ordering.
    """
    queryset = Server.objects.all().order_by('-last_checked')
    serializer_class = ServerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'name', 'ip_address']
    search_fields = ['name', 'url', 'ip_address']
    ordering_fields = ['last_checked', 'response_time']
    permission_classes = [IsAuthenticated] 
    

class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API View to retrieve, update, or delete a server.
    - Requires authentication.
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [IsAuthenticated]


class ServerStatusHistoryListView(generics.ListAPIView):
    """
    API View to list server status history.
    - Can filter by server ID.
    - Read-only access.
    """
    serializer_class = ServerStatusHistorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['server', 'status']
    ordering_fields = ['checked_at']
    ordering = ['-checked_at']

    def get_queryset(self):
        return ServerStatusHistory.objects.all()


class AlertLogListView(generics.ListAPIView):
    """
    API View to list alert logs.
    - Can filter by server.
    - Read-only access.
    """
    serializer_class = AlertLogSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['server']
    ordering_fields = ['sent_at']
    ordering = ['-sent_at']

    def get_queryset(self):
        return AlertLog.objects.all()
