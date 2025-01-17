from django.shortcuts import render
from .models import Subscription
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import SubscriptionSerializer
from django.db.models import Prefetch, F, Sum
from clients.models import Client
from rest_framework.response import Response



class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name', 'user__email')),
    )#.annotate(
        #price=F("service__full_price") - (F("service__full_price") * F("plan__discount_percent") / 100
                                          #))
    serializer_class = SubscriptionSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        response_data = {"result:" : response.data}
        response_data["total_amount"] = queryset.aggregate(total=Sum('price')).get('total')
        response = Response(response_data)
        return response
