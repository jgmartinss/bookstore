from django.urls import path

from django.utils.translation import gettext_lazy as _

from bookstore.apps.orders import views as order_view

from . import views


app_name = "checkout"

urlpatterns = [
    path(
    	"cart/", 
    	views.cart_detail, 
    	name="cart_detail"
    ),
    path(
    	"add/<int:product_id>/", 
    	views.cart_add, 
    	name="cart_add"
    ),
    path(
    	"remove/<int:product_id>/", 
    	views.cart_remove, 
    	name="cart_remove"
    ),
    path(
    	"onepage/", 
    	order_view.create_order, 
    	name="cart_onepage"
    ),
    path(
        "onepage/success/",
        order_view.OrderSuccessView.as_view(),
        name="cart_onepage_success",
    ),
]
