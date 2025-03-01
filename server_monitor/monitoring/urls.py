from django.urls import path
from .views import (
    ServerListCreateView, 
    ServerDetailView, 
    ServerStatusHistoryListView, 
    AlertLogListView
)

urlpatterns = [
    # Server Endpoints
    path('servers/', ServerListCreateView.as_view(), name='server-list'),
    path('servers/<int:pk>/', ServerDetailView.as_view(), name='server-detail'),

    # Server Status History
    path('servers/<int:pk>/history/', ServerStatusHistoryListView.as_view(), name='server-status-history'),

    # Alert Logs
    path('servers/<int:pk>/alerts/', AlertLogListView.as_view(), name='server-alerts'),
]
