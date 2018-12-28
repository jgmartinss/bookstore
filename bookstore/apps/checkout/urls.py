from django.urls import path

from django.utils.translation import gettext_lazy as _

from . import views


app_name = 'checkout'

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    # path('onepage/', views.cart_onepage, name='cart_onepage'),
]
