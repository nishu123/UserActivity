from django.urls import path, include

app_name = "customer"

urlpatterns = [
path('customer/login/', views.Login, name="login"),

]