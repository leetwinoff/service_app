from rest_framework import serializers
from .models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ['id', 'plan_type', 'discount_percent']



class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    clients_name = serializers.CharField(source='client.company_name', read_only=True)
    email = serializers.CharField(source='client.user.email', read_only=True)
    class Meta:
        model = Subscription
        fields = ['id', 'plan_id', 'clients_name', 'email', 'plan']