from django.shortcuts import render

from django.views import generic

from bookstore.apps.checkout.cart import Cart
from bookstore.apps.catalog.models import Book


class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context["last_products"] = self.get_last_products
        context["best_products"] = {}
        context["top_product"] = {}
        return context

    def get_last_products(self):
        return Book.objects.all().order_by("-created")[:4]

    def get_best_products(self):
        # retornar os 4 mais vendidos
        pass

    def get_top_product(self):
        # retornar o produto mais vendido
        pass


def cart_len(request):
    cart = Cart(request)
    return render(request, "partials/nav.html", {"cart": cart})
