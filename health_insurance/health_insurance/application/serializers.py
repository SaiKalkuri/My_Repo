from rest_framework import serializers
from . models import Customer,Premium,Claims,Expanses

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields ="__all__"

class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium
        fields ="__all__"

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claims
        fields ="__all__"

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expanses
        fields ="__all__"

        