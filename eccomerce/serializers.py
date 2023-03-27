from rest_framework import serializers
from .models import Product,OrderDetail,Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('id','name','price','stock')

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields=('id','order_id','quantity','product_id')
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields=('id','date','client')