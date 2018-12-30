from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from bookstore.apps.checkout.cart import Cart

from bookstore.apps.accounts.models import User
from bookstore.apps.orders.models import OrderItem
from bookstore.apps.orders.forms import OrderForm 

from decimal import Decimal


@login_required
def create_order(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderForm(request.user, request.POST)
		user = User.objects.filter(id=request.user.id)
		if form.is_valid():
			order = form.save(commit=False)
			order.user = request.user
			order.save()
			for item in cart:
				real_price = Decimal(item['price']) * int(item['quantity'])
				OrderItem.objects.create(
					order=order, product=item['product'], 
					price=real_price, quantity=item['quantity']
				)
			cart.clear()
			request.session['order_id'] = order.id
			return redirect('/')
	else:
		form = OrderForm(request.user)
		user = User.objects.filter(id=request.user.id)
	return render(
    	request, 
    	'checkout/onepage.html', 
    	{'form': form, 'user': user, 'cart': cart}
    )
