from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('developer', 'Developer'),
        ('it_staff', 'IT Team Member'),
        ('ebanking_support', 'Ebanking Support Team Member'),
        ('customer_engagement', 'Customer Engagement Team Member'),
        ('flexipay', 'Fexipay Support'),
        ('user', 'User'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    def is_admin(self):
        return self.role == 'admin'

    def is_developer(self):
        return self.role == 'developer'

    def is_it_staff(self):
        return self.role == 'it_staff'
    
    def is_flexipay(self):
        return self.role == 'flexipay'
    
    def is_customer_engagement(self):
        return self.role == 'customer_engagement'
    
    def is_ebanking_support(self):
        return self.role == 'ebanking_support'

