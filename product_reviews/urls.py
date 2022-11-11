from django.contrib import admin
from django.urls import path, include
from . import views
from products.models import Products


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('/', include('product_reviews.urls'))
# ]

urlpatterns = [
    path('', views.review_list),
    path('<int:pk>/', views.review_detail),
    path('by_product/<int:product_id>/', views.review_by_product)
]