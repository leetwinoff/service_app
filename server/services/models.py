from django.db import models
from django.core.validators import MaxValueValidator
from clients.models import Client

class Service(models.Model):
    name = models.CharField(max_length=100)
    full_price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.full_price}$"


class Plan(models.Model):
    PLAN_TYPES = [
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    ]

    plan_type = models.CharField(max_length=10, choices=PLAN_TYPES)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    def __str__(self):
        return f'{self.plan_type} plan'



class Subscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='subscriptions')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name='subscriptions')

    def __str__(self):
        return f'{self.client.company_name} - {self.service} - {self.plan}'