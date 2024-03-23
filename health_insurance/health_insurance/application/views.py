from . models import Customer,Premium,Claims,Expanses
from . serializers import CustomerSerializer,PremiumSerializer,ClaimSerializer,ExpenseSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs).data
        user_id = request.user.id if request.user.is_authenticated else None
        customer_instance = Customer.objects.get(pk=data.get('id'))
        if user_id is not None:
            user_instance = User.objects.get(pk=user_id)
            customer_instance.created_by = user_instance
        else:
            customer_instance.created_by = None
        customer_instance.save()
        result = {"msg": "data added successfully", "id": customer_instance.id}
        return Response(result)
    
    def update(self, request, pk=None, *args, **kwargs):
        data = super().update(request, pk=pk, *args, **kwargs).data
        result = {"msg": "data not updated", "id": ""}
        
        user = request.user

        # Get the customer instance
        customer_instance = Customer.objects.get(pk=pk)

        # Check if the user is authenticated
        if user.is_authenticated:
            # Set updated_by to the user instance
            customer_instance.updated_by = user
        else:
            # Set updated_by to None if user is not authenticated
            customer_instance.updated_by = None

        # Save the changes
        customer_instance.save()

        result = {"msg": "data updated successfully", "id": customer_instance.id}
        return Response(result)
    

class PremiumView(viewsets.ModelViewSet):
    queryset = Premium.objects.all()
    serializer_class=PremiumSerializer

class ClaimsView(viewsets.ModelViewSet):
    queryset = Claims.objects.all()
    serializer_class=ClaimSerializer

class ExpenseView(viewsets.ModelViewSet):
    queryset=Expanses.objects.all()
    serializer_class=ExpenseSerializer
    
class Profit_loss(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        total_premium=Premium.objects.all().aggregate(Sum('premium_amount'))['premium_amount__sum'] or 0
        total_claims=Claims.objects.all().aggregate(Sum('claim_amount'))['claim_amount__sum'] or 0
        total_expenses=Expanses.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0
        profit_loss=total_premium-total_claims-total_expenses
        data={
            "total_premium":total_premium,
            "total_claims":total_claims,
            "total_expenses":total_expenses,
            "profit_loss":profit_loss
        }
        return Response(data)
    
    

