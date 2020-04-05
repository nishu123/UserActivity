from django.urls import path
from userapp.api.views import *
# from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    # path('', api_detail_customer_view, name="detail"),
    # path('update/', api_update_customer_view, name="update"),
     path('list/', MemberActivity, name="detail"),
   

   
]