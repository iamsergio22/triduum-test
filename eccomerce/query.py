from django.db.models import Sum
from models import OrderDetail
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eccomerce.settings")
import django
django.setup()

producto_mas_ordenado = OrderDetail.objects.values('producto').annotate(cantidad_total=Sum('cantidad')).order_by('-cantidad_total').first()

print(f"El producto más ordenado es {producto_mas_ordenado['producto']} con una cantidad total de {producto_mas_ordenado['cantidad_total']}.")
