## PASOS PARA INICIAR EL PROYECTO: <br>
1. python -m venv env -> Crear entorno virtual.<br>
2. .\env\Scripts\activate -> activar entorno.<br>
3. pip install -r requirements.txt.<br>

### Endpoints: 
/orders/add/ <br>
/orders/get/ <br>
/orders/54/ <br>
/orders/1/update/ <br>
/orders/1/delete/ <br>
/products/get/ <br>
/products/6 <br>
/products/add/ <br>
/products/6/update/ <br>
/products/5/delete/ <br>
/order-detail/ <br>
### Consulta SQL (Raw Query u ORM) que permita saber cual es el producto que más ha sido ordenado y en qué cantidades:
1. Ejecutar python manage.py shell
2. from django.db.models import Sum
3. from eccomerce.models import Order
4. from eccomerce.models import OrderDetail
5. from eccomerce.models import Product
6. product_max=OrderDetail.objects.values('product_id').annotate(total_cantidad=Sum('quantity')).order_by('-total_cantidad').first()
7. print(product_max) <br><br>

![image](https://user-images.githubusercontent.com/101826187/227840127-4121700a-3033-41b0-98d0-040b40753208.png)
![image](https://user-images.githubusercontent.com/101826187/227840216-cf27fe50-b736-475f-9a4d-6bf39de26e48.png)
![image](https://user-images.githubusercontent.com/101826187/227840252-55e62180-619d-4474-91eb-ce91ac2ea553.png)
![image](https://user-images.githubusercontent.com/101826187/227840273-d908e99c-ccff-45b0-9e76-a7b0cac084c0.png)
![image](https://user-images.githubusercontent.com/101826187/227840292-9a8b764b-e596-4736-b13a-f50bab89d74b.png)
![image](https://user-images.githubusercontent.com/101826187/227840307-027a7b22-39d3-4e90-8470-abe386525bf9.png)


