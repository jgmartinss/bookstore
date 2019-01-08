from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

from bookstore.apps.checkout.cart import Cart

from bookstore.apps.accounts.models import User
from bookstore.apps.orders.models import OrderItem, Order
from bookstore.apps.orders.forms import OrderForm

from decimal import Decimal


@login_required
def create_order(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderForm(request.user, request.POST)
        user = User.objects.filter(id=request.user.id)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                real_price = Decimal(item["price"]) * int(item["quantity"])
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=real_price,
                    quantity=item["quantity"],
                )
            cart.clear()
            request.session["order_id"] = order.id
            return redirect("checkout:cart_onepage_success")
    else:
        form = OrderForm(request.user)
        user = User.objects.filter(id=request.user.id)
    return render(
        request, "checkout/onepage.html", {"form": form, "user": user, "cart": cart}
    )


class OrderSuccessView(LoginRequiredMixin, generic.TemplateView):
    template_name = "checkout/success.html"

    def get_context_data(self, **kwargs):
        context = super(OrderSuccessView, self).get_context_data(**kwargs)
        context["order"] = self.get_order_number
        return context

    def get_order_number(self):
        return Order.objects.filter(user__id=self.request.user.id).order_by("-id")[:1][
            ::-1
        ]
