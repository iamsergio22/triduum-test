from .models import Product, Order, OrderDetail
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import ProductSerializer, OrderDetailSerializer, OrderSerializer
from rest_framework.decorators import action
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'], url_path='get')
    def get_products(self, request):
        Orders = Product.objects.all()
        serializer = ProductSerializer(Orders, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='add')
    def add_products(self, request, *args, **kwargs):
        data = request.data

        order = Product.objects.create(
            name=data['name'],
            price=data['price'],
            stock=data['stock']
        )
        serializer = self.get_serializer(order)
        return Response({'status': 'product created'})

    @action(detail=True, methods=['put'], url_path='update')
    def update_product(self, request, pk):
        data = request.data
        order = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=order, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_products(self, request, pk):
        try:
            order = Product.objects.get(id=pk)
            order.delete()
            return Response({"msg": "product deleted"})
        except ObjectDoesNotExist:
            return Response({"msg":"Product not exist"})
# --------------------------------------------------------------Order--------------------------------------------


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer

    @action(detail=False, methods=['get'], url_path='get')
    def get_orders(self, request):
        Orders = Order.objects.all()
        serializer = OrderSerializer(Orders, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='add')
    def add_orders(self, request, *args, **kwargs):
        if request.method != 'POST':  # Verifica si el método no es POST
            return Response({'status': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        data = request.data

        order = Order.objects.create(
            date=data['date'],
            client=data['client']
        )

        for product_data in data['products']:
            try:
                product = Product.objects.get(id=product_data['product'])
            except Product.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': f'No se encontró un objeto Product con id={product_data["product"]}'}, status=400)
            OrderDetail.objects.create(
                order_id=order,
                product_id=product,
                quantity=product_data['quantity']
            )

        serializer = self.get_serializer(order)
        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'order created'})

    @action(detail=True, methods=['put'], url_path='update')
    def update_order(self, request, pk):
        data = request.data
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(instance=order, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_order(self, request, pk):
        try:
            order = Order.objects.get(id=pk)
            order.delete()
            return Response({"msg":"Product deleted"})
        except ObjectDoesNotExist:
            return Response({"msg":"Product not exist"})


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderDetailSerializer
