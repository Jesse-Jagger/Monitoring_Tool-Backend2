from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """ Grants access only to Admin users """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsDeveloper(BasePermission):
    """ Grants access only to Developer users """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'developer'

class IsITStaff(BasePermission):
    """ Grants access only to IT Staff """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'it_staff'

class IsEbankingSupport(BasePermission):
    """ Grants access only to Ebanking Support """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'ebanking_support'

class IsFlexipay(BasePermission):
    """ Grants access only to Flexipay Support """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'flexipay_support'
    
class IsCustomerEngagement(BasePermission):
    """ Grants access only to Customer Engagement Team """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Customer_Engagement'
