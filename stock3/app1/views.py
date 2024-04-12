from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
import jwt
import pdb
from app1.authentications import MyAuthentication
from django.contrib.auth.models import User
from rest_framework import HTTP_HEADER_ENCODING,exceptions
from django.conf import settings


class LoginView(APIView):
    authentication_classes=[]
    permission_classes=[]

    def post(self,request):
        
        

        data=request.data
        rel_data={'token':None,'msg':''}
        
        user =authenticate(**data)
        if user:
            payload=request.data
            jtoken=jwt.encode(payload,'django-insecure-75zotega+o)b-bh433r*1(&jq9985*ng^o0$cl4_+f03*va-0+'
,algorithm='HS256')
            # token_instance =Token.objects.get_or_create(user=user)[0]
            rel_data['token']=jtoken
            rel_data["msg"]='token generated'
            return Response(rel_data)
        else:
            return Response(rel_data,status=status.HTTP_403_FORBIDDEN)
 

class CategoryView(APIView):
    
    def post(self,request):
        req = CategorySerializer(data=request.data)
        
        msg = ""
        if req.is_valid():
            req.save()
            msg = "Added Successfully"
            status_code = status.HTTP_201_CREATED
        else:
          
            msg = req.errors
            status_code = status.HTTP_400_BAD_REQUEST
        
        return Response({"Result":msg, "data":request.data}, status=status_code)
    
    def get(self, request, id=None):
        if id == None:
            data = Category.objects.all()
            res = CategorySerializer(data, many=True)
            return Response(res.data)
        else:
            data = Category.objects.get(id=id)
            res = CategorySerializer(data)
            return Response(res.data)

class ProductView(APIView):
    def post(self, request):
        req = ProductSerializer(data=request.data)
        msg = ""
        data1={}
        if req.is_valid():
            data = req.save()

            data1 = req.data
            data1.update({"id":data.id})
            data.openingstock_set.create(opening_stock=request.data.get("opening_stock"))
            msg = "Added Successfully"
            status_code = status.HTTP_201_CREATED
        else:
            msg = req.errors
            status_code = status.HTTP_400_BAD_REQUEST
        
        return Response({"Result":msg, "data":data1}, status=status_code)
    
    def get(self, request, id=None):

        if id == None:
            data = Product.objects.all()
            res = ProductSerializer(data, many=True)
            return Response(res.data)
        else:
            data = Product.objects.get(id=id)
            res = ProductSerializer(data)
            return Response(res.data)

class PurchaseView(APIView):
    def post(self, request):
        purchase = []
        for i in request.data:
            req = PurchaseSerializer(data=i)
            # import pdb;pdb.set_trace()
            msg=""
            if req.is_valid():
                s = req.save()
                data = req.data
                data.update({"id":s.id})
                purchase.append(data)
                msg = "Added Successfully"
                status_code = status.HTTP_201_CREATED
            else:
                msg = req.errors
                status_code = status.HTTP_400_BAD_REQUEST
        
        return Response({"Result":msg, "data":purchase}, status=status_code)
    
    def get(self, request, id=None):
        if id == None:
            data = Purchase.objects.all()
            res = PurchaseSerializer(data, many=True)
            return Response(res.data)
        else:
            data = Purchase.objects.get(id=id)
            res = PurchaseSerializer(data)
            return Response(res.data)

class SalesView(APIView):
    def post(self, request):
        sales =[]
        for i in request.data:
            req = SalesSerializer(data=i)
            msg=""
            if req.is_valid():
                s = req.save()
                data = req.data
                data.update({"id":s.id})
                sales.append(data)
                msg = "Added Successfully"
                status_code = status.HTTP_201_CREATED
            else:
                msg = req.errors
                status_code = status.HTTP_400_BAD_REQUEST
        
        return Response({"Result":msg, "data":sales}, status=status_code)
    
    def get(self, request, id=None):
        if id == None:
            data = Sales.objects.all()
            res = SalesSerializer(data, many=True)
            return Response(res.data)
        else:
            data = Sales.objects.get(id=id)
            res = SalesSerializer(data)
            return Response(res.data)
    

class StockView(APIView):
    def get(self,request,id=None):
        if id == None:
            main = []
            for cat in Category.objects.all():
                category = {}
                for pro in Product.objects.all():
                    if pro.category_id == cat.id:
                        category["category_name"]=cat.name
                    products=[]    
                    for product in Product.objects.all():
                        pro={}
                        if product.category_id == cat.id:
                            pro["id"] = product.id
                            pro["name"]=product.name
                            pro["unique_number"]=product.unique_num 
                        if len(pro) == 0:
                            pass
                        else:
                           for op in OpeningStock.objects.all():
                            stock={}
                            if op.product_id == product.id:
                                pro["opening_stock"]=op.opening_stock
                            
                            for pur in Purchase.objects.all():
                                if pur.product_id == product.id:
                                    pro["purchase_stock"]=pur.stock
                            for sale in Sales.objects.all():
                                if sale.product_id == product.id:
                                    pro["sales_stock"]=sale.stock
                            
                            for i in range(len(Product.objects.all())):
                                if pro.get("opening_stock") == None:
                                    pro["opening_stock"] = 0 
                                if pro.get("sales_stock") == None:
                                    pro["sales_stock"] = 0
                                if pro.get("purchase_stock") == None:   
                                    pro["purchase_stock"] = 0
                                
                                pro["remaining_stock"] = pro.get("opening_stock")+pro.get("purchase_stock")-pro.get("sales_stock")
                           products.append(pro)
                    category["products"]=products      
                main.append(category)
            return Response(main)
        else:
            cat = Category.objects.get(id=id)
            category = {}
            for pro in Product.objects.filter(category_id=id):
                if pro.category_id == id:
                    category["category_name"]=cat.name
                products=[]    
                for product in Product.objects.filter(category_id=id):
                    pro={}
                    if product.category_id == id:
                        pro["id"] = product.id
                        pro["name"]=product.name
                        pro["unique_number"]=product.unique_num 
                    if len(pro) == 0:
                        pass
                    else:
                        for op in OpeningStock.objects.filter(id=product.id):
                            
                            if op.product_id == product.id:
                                pro["opening_stock"]=op.opening_stock
                                
                        for pur in Purchase.objects.filter(id=product.id):
                            if pur.product_id == product.id:
                                 pro["purchase_stock"]=pur.stock

                        for sale in Sales.objects.filter(id=product.id):
                            if sale.product_id == product.id:
                                pro["sales_stock"]=sale.stock
                                
                        for i in range(len(Product.objects.filter(id=product.id))):
                            if pro.get("opening_stock") == None:
                                pro["opening_stock"] = 0 
                            if pro.get("sales_stock") == None:
                                pro["sales_stock"] = 0
                            if pro.get("purchase_stock") == None:   
                                pro["purchase_stock"] = 0
                                    
                            pro["remaining_stock"] = pro.get("opening_stock")+pro.get("purchase_stock")-pro.get("sales_stock")
                            products.append(pro)
                        category["products"]=products      
                
            return Response(category)


               
           

