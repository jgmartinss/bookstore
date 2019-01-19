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


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    context_object_name = "orders"
    paginate_by = 6
    template_name = "orders/list_orders.html"

    def get_queryset(self, **kargs):
        order_dict = {}
        context = []
        total = "$200fake"
        orders = Order.objects.filter(user=self.request.user).order_by("-created")

        for order in orders:
            full_name = "{} {}".format(order.user.first_name, order.user.last_name)

            order_dict = {
                "id": order.id,
                "date": order.created,
                "shipto": full_name,
                "total": total,
                "status": order.status,
            }
            context.append(order_dict)
        return context
