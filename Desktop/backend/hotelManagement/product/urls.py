from django.contrib import admin
from product import views
from product.views import *
from django.urls import include
from django.urls import re_path as url

urlpatterns = [
    url("login/", login),
    url("sign_up/", sign_up),
    url("logout/", Logout.as_view()),
    url(r'^cart/(?P<cart_id>[0-9]+)$',views.CartViewSet.as_view()),
	url(r'cart/',views.CartViewSet.as_view()),
    url(r'^category/(?P<category_id>[0-9]+)$',views.CategoryViewSet.as_view()),
	url(r'category/',views.CategoryViewSet.as_view()),
    url(r'^product/(?P<product_id>[0-9]+)$',views.ProductViewSet.as_view()),
	url(r'product/',views.ProductViewSet.as_view()),
]