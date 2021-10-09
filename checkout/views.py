from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))  # ToPreventAccessURLVia:/checkout

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JXrzrLnyR6DXdiZl7ZnPYzmSvocKqe0y49b23XtjEFJaaS8cCQaNqKcHVITcG2o8IABfFvUPEKo2hsJAlwjgpbK00AjJflhCA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
