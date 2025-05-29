# from django.utils.deprecation import MiddlewareMixin
# from locust import HttpUser

# class JWTAuthMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         token = request.session.get("access_token", None)
#         if token:
#             request.META["HTTP_AUTHORIZATION"] = f"Bearer {token}"  # ✅ Передаём токен в заголовке


#     def get_token_from_session(self, request):
#         """Получаем токен из сессии пользователя"""
#         return request.session.get("access_token", "")

# ADMIN_IPS = ["192.168.1.10", "192.168.1.20"]

# class AdminIPBypassMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         ip = request.META.get("REMOTE_ADDR")

#         if ip in ADMIN_IPS:
#             request.META["HTTP_AUTHORIZATION"] = f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ4NTMxMjk2LCJpYXQiOjE3NDg0NDQ4OTYsImp0aSI6ImQ1NDAwNGZlM2ZmOTRlY2ZhZTMwNTMwOWM3ZjcwNDg0IiwidXNlcl9pZCI6MX0.b_fJ9uSgTqE3AhaqUe_cROfur_HKIx_EZth0BdH3944"  # Упрощаем доступ

#         return self.get_response(request)
    
# class WebsiteUser(HttpUser):
#     def on_start(self):
#         self.access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ4NTMxMjk2LCJpYXQiOjE3NDg0NDQ4OTYsImp0aSI6ImQ1NDAwNGZlM2ZmOTRlY2ZhZTMwNTMwOWM3ZjcwNDg0IiwidXNlcl9pZCI6MX0.b_fJ9uSgTqE3AhaqUe_cROfur_HKIx_EZth0BdH3944"

#     @task
#     def get_products(self):
#         headers = {"Authorization": f"Bearer {self.access_token}"}
#         self.client.get("/api/products/", headers=headers)
