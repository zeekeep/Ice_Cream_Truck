import re
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Customer,Cart,Product,Category
from .serializers import CustomerSerializer,CartSerializer,ProductSerializer,CategorySerializer
from django.http import JsonResponse
# login API for user login with token genration(DRF)
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response(
            {"error": "Please provide both username and password"},
            status=HTTP_400_BAD_REQUEST,
        )
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key}, status=HTTP_200_OK)


# logout API for user logout
class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response("You have successfully logged out!", status=status.HTTP_200_OK)


# user sign up/registration API
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def sign_up(request):
    serialized = CustomerSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        response = {
            "status": "success",
            "code": status.HTTP_201_CREATED,
            "message": "You have successfully register user!",
            "data": [],
        }
        return Response(response)
    else:
        response = {
            "status": "success",
            "code": status.HTTP_400_BAD_REQUEST,
            "message": serialized._errors,
            "data": [],
        }
        return Response(response)


class CategoryViewSet(APIView):
	
	def post(self,request):
		try:
			category_data = CategorySerializer(data=request.data)
			if not(category_data.is_valid()):
				return Response(category_data.errors)
			category_data.save()
			return Response("Category created successfully",status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error while creating Category")

	def get(self,request,category_id=None):
		try:
			if(category_id):
				category_data = Category.objects.filter(pk=category_id,is_deleted = False)[0]
				get_data = CategorySerializer(category_data)
			else:
				category_data = Category.objects.filter(is_deleted = False)
				get_data = CategorySerializer(category_data,many=True)
			return Response(get_data.data,status=status.HTTP_200_OK)
		except Exception as err: 
			print(err) 
			return Response("Error : Data Not Found")


	def put(self,request,category_id):
		try:
			get_data = Category.objects.get(pk=category_id)
			update_data = CategorySerializer(get_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return Response("Category details updated Successfully")
			else:
				return Response(update_data.errors)	
		except:
			return Response("Error : Data Not Found")

	def delete(self,request,category_id):
		try:
			Category.objects.filter(pk=category_id).update(is_deleted = True)
			return Response("Category Deleted Successfully",status=status.HTTP_200_OK)
		except Exception as err:
			print(err)    
			return Response("Error while deleting the Category",500)

class ProductViewSet(APIView):
	
	def post(self,request):
		try:
			product_data = ProductSerializer(data=request.data)
			if not(product_data.is_valid()):
				return Response(product_data.errors)
			product_data.save()
			return Response("Product created successfully",status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error while creating product")

	def get(self,request,product_id=None):
		try:
			if(product_id):
				product_data = Product.objects.filter(pk=product_id,is_deleted = False)[0]
				get_data = ProductSerializer(product_data)
			else:
				product_data = Product.objects.filter(is_deleted = False)
				get_data = ProductSerializer(product_data,many=True)
			return Response(get_data.data,status=status.HTTP_200_OK)
		except Exception as err: 
			print(err) 
			return Response("Error : Data Not Found")


	def put(self,request,product_id):
		try:
			get_data = Product.objects.get(pk=product_id)
			update_data = ProductSerializer(get_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return Response("Product details updated Successfully")
			else:
				return Response(update_data.errors)	
		except:
			return Response("Error : Data Not Found")

	def delete(self,request,product_id):
		try:
			Product.objects.filter(pk=product_id).update(is_deleted = True)
			return Response("Product Deleted Successfully",status=status.HTTP_200_OK)
		except Exception as err:
			print(err)    
			return Response("Error while deleting the Product",500)
  
class CartViewSet(APIView):
    
    def get(self, request):
        current_user = request.user
        item_quantity = [user.item_quantity for user in Cart.objects.all()]
        item = [user.item for user in Cart.objects.all()]
        price=re.findall("\d+\.\d+",str(item))
        total_cost = item_quantity[0] * float(price[0])
        return JsonResponse(total_cost, safe=False)
    
