from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from users.serializers import UserSerializer, LoginSerializer
from users.permissions import ( 
    IsAdmin, 
    IsDeveloper,  
    IsITStaff,
    IsCustomerEngagement,
    IsEbankingSupport,
    IsFlexipay
)

User = get_user_model()

# Register new user (Restricted to Admins, IT_Support, Developers and Ebanking_Support )
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsITStaff | IsDeveloper | IsEbankingSupport)]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# Login view with JWT token generation (Public)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.customuser.role  # Ensure role is included
                },
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logout view - blacklist refresh token (Authenticated)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

# Retrieves & updates user profile (Authenticated users only)
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Prevents unauthorized access to other users

# User Management (Restricted to Admins)
class UserManagementView(APIView):
    permission_classes = [IsAuthenticated & (IsAdmin | IsITStaff | IsDeveloper | IsEbankingSupport)]

    def get(self, request):
        return Response({"message": "User Management Access Granted"})

# Server Management (Admins, IT Staff, Developers & Ebanking)
class ServerManagementView(APIView):
    permission_classes = [IsAuthenticated & (IsAdmin | IsITStaff | IsDeveloper | IsEbankingSupport)]

    def get(self, request):
        return Response({"message": "Server Management Access Granted"})

# Real-Time Server Status (All)
class RealTimeServerStatusView(APIView):
    permission_classes = [IsAuthenticated & (IsAdmin | IsITStaff | IsDeveloper | IsCustomerEngagement | IsFlexipay | IsEbankingSupport)]

    def get(self, request):
        return Response({"message": "Real-Time Server Status Access Granted"})

# Server Logs (Admins, IT Staff, Developers, Customer Engagement)
class ServerLogsView(APIView):
    permission_classes = [IsAuthenticated & (IsAdmin | IsITStaff | IsDeveloper | IsFlexipay)]

    def get(self, request):
        return Response({"message": "Server Logs Access Granted"})

# Alerts (All)
class AlertsView(APIView):
    permission_classes = [IsAuthenticated & (IsAdmin | IsITStaff | IsDeveloper | IsFlexipay | IsEbankingSupport | IsCustomerEngagement)]

    def get(self, request):
        return Response({"message": "Alerts Access Granted"})

# Reports (All)
class ReportsView(APIView):
    permission_classes = [IsAuthenticated & (IsAdmin | IsITStaff | IsDeveloper | IsFlexipay | IsEbankingSupport | IsCustomerEngagement)]

    def get(self, request):
        return Response({"message": "Reports Access Granted"})

# Admin Dashboard (Restricted to Admins, developers, IT & Ebanking)
class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated & (IsAdmin | IsITStaff | IsDeveloper | IsEbankingSupport)]

    def get(self, request):
        return Response({"message": "Admin Dashboard Access Granted"})

# System Settings (Restricted to Admins, Developers IT and Ebanking)
class SystemSettingsView(APIView):
    permission_classes = [IsAuthenticated & (IsAdmin | IsITStaff | IsDeveloper | IsEbankingSupport)]

    def get(self, request):
        return Response({"message": "System Settings Access Granted"})

# API Access (Admins & Developers)
class APIAccessView(APIView):
    permission_classes = [IsAuthenticated & (IsAdmin | IsDeveloper)]

    def get(self, request):
        return Response({"message": "API Access Granted"})

# Codebase Access (Admins & Developers)
class CodebaseAccessView(APIView):
    permission_classes = [IsAuthenticated & (IsAdmin | IsDeveloper)]

    def get(self, request):
        return Response({"message": "Codebase Access Granted"})

