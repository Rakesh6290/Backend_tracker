from django.db import models
from django.conf import settings

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Offer', 'Offer'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    source = models.CharField(max_length=50, blank=True)
    job_link = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    applied_date = models.DateField()
    follow_up_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
