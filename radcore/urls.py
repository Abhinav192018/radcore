from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('products/', views.products, name='products'),
    path('product/details/', views.product_detail, name='product_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
  
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)