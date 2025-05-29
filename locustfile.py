from locust import HttpUser, task, between

class EleganzaUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_staff(self):
        """Тестируем `GET /api/staff/`"""
        self.client.get("/api/staff/")

    @task
    def post_transaction(self):
        self.client.post("/api/transactions/", json={
            "amount": 500,  
            "status": "pending"  # ✅ Должно соответствовать модели `Transaction`
    })


    @task
    def get_categories(self):
        """Тестируем `GET /api/categories/`"""
        self.client.get("/api/categories/")

    @task
    def post_category(self):
        """Тестируем `POST /api/categories/`"""
        self.client.post("/api/categories/", json={"name": "New Category"})

    @task
    def get_products(self):
        """Тестируем `GET /api/products/`"""
        self.client.get("/api/products/")

    @task
    def post_product(self):
        """Тестируем `POST /api/products/`"""
        self.client.post("/api/products/", json={
            "name": "New Product",
            "price": 99.99,
            "stock": 10,
            "description": "Описание продукта",
            "category": 1
        })

    @task
    def get_deliveries(self):
        """Тестируем `GET /api/deliveries/`"""
        self.client.get("/api/deliveries/")

    @task
    def post_delivery(self):
        """Тестируем `POST /api/deliveries/`"""
        self.client.post("/api/deliveries/", json={
            "staff": 1,
            "begin_date": "2025-05-29T12:00:00Z",
            "status": "pending",
            "transport": 1,
            "price": 250.50
        })

    @task
    def get_finance(self):
        """Тестируем `GET /api/finance/`"""
        self.client.get("/api/finance/")

    @task
    def get_income(self):
        """Тестируем `GET /api/income/`"""
        self.client.get("/api/income/")

    @task
    def get_expenses(self):
        """Тестируем `GET /api/expenses/`"""
        self.client.get("/api/expenses/")

    @task
    def get_shipment(self):
        """Тестируем `GET /api/shipment/`"""
        self.client.get("/api/shipment/")
