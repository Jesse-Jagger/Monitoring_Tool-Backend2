from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('developer', 'Developer'),
        ('project_manager', 'Project Management Team Member'),
        ('it_staff', 'IT Team Member'),
        ('ebanking_support', 'Ebanking Support Team Member'),
        ('customer_engagement', 'Customer Engagement Team Member')
        ('flexipay', 'Fexipay Support')
        ('user', 'User'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    def is_admin(self):
        return self.role == 'admin'

    def is_developer(self):
        return self.role == 'developer'

    def is_project_manager(self):
        return self.role == 'project_manager'

    def is_it_staff(self):
        return self.role == 'it_staff'
    
    def is_flexipay(self):
        return self.role == 'flexipay'
    
    def is_customer_engagement(self):
        return self.role == 'customer_engagement'
    
    def is_ebanking_support(self):
        return self.role == 'ebanking_support'

