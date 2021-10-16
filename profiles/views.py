"""
Views of the profiles app
"""
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from products.models import Product

from .models import UserProfile, WishList
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile_user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile_user)
    orders = profile_user.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """Display order history"""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@ login_required
def wishlist(request):
    """
    A view to show the wishlist
    """
    wish_list = get_object_or_404(WishList, user=request.user)
    template = 'profiles/wishlist.html'
    context = {
        'wishlist': wish_list
    }

    return render(request, template, context)


@ login_required
def add_to_wishlist(request, user_id, product_id):
    """
    Adding a product to the wish list
    """
    w_list = get_object_or_404(WishList, pk=user_id)
    product = get_object_or_404(Product, pk=product_id)
    if product.w_list.filter(id=request.user.id):
        product.w_list.remove(request.user)
    else:
        product.w_list.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@ login_required
def delete_from_wishlist(request, product_id):
    """
    Delete a product from the wishlist
    """
    if not request.user.is_logged_in(user=request.user.id):
        messages.error(
            request, 'Sorry, only logged in account users can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted from Wish List!')
    return redirect(reverse('wishlist'))
