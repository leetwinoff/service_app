from django.shortcuts import render
from .models import Subscription
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import SubscriptionSerializer
from django.db.models import Prefetch
from clients.models import Client


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name', 'user__email')),
    )
    serializer_class = SubscriptionSerializer

