from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Базовая модель для наследования

class Category(BaseModel):
    name = models.CharField(max_length=255)

class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Delivery(BaseModel):
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    begin_date = models.DateTimeField()
    delivered_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Ожидание'), ('completed', 'Завершено')])
    transport = models.ForeignKey('Transport', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Staff(BaseModel):
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

class Payroll(BaseModel):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()

class Suppliers(BaseModel):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.TextField()
    type_material = models.CharField(max_length=255)

class Transport(BaseModel):
    model = models.CharField(max_length=255)
    capacity = models.IntegerField()
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

class Shipment(BaseModel):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    status = models.CharField(max_length=50, choices=[('pending', 'Ожидание'), ('completed', 'Доставлено')])
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Accessories(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

class Finance(BaseModel):
    income = models.ForeignKey('Income', on_delete=models.CASCADE)
    expense = models.ForeignKey('Expenses', on_delete=models.CASCADE)

class Transaction(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Ожидание'), ('completed', 'Завершено')])
    created_at = models.DateTimeField(auto_now_add=True)

class Income(BaseModel):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()

class Expenses(BaseModel):
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()



