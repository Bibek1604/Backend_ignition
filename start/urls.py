from django.urls import path
from django.contrib import admin
from API.views import ProductAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductAPIView.as_view(), name='product-api'),
    # Add other API paths if needed
]