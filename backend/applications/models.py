from django.conf import settings
from django.db import models


class JobApplication(models.Model):
    class Status(models.TextChoices):
        APPLIED = 'applied', 'Applied'
        INTERVIEW = 'interview', 'Interview'
        OFFER = 'offer', 'Offer'
        REJECTED = 'rejected', 'Rejected'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='applications',
    )
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    date_applied = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.APPLIED,
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.position} @ {self.company_name}'
