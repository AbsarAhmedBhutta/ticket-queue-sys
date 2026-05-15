from django.db import models
from django.contrib.auth.models import User

class SupportUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class SupportStaff(models.Model):
    DEPARTMENT_CHOICES = [
        ('TECH', 'Tech'),
        ('BILLING', 'Billing'),
        ('SALES', 'Sales'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='TECH')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
    class Priority(models.TextChoices):
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"
    
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        IN_PROGRESS = "in_progress", "In Progress"
        RESOLVED = "resolved", "Resolved"
        
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_by = models.ForeignKey(SupportUser, on_delete=models.CASCADE,  null=True, blank=True)
    assigned_to = models.ForeignKey(SupportStaff, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    