"""
Views of the profiles app
"""
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from checkout.models import Order
from products.models import Product

from .models import Review, UserProfile, WishList
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
    user = UserProfile.objects.filter(user=request.user)
    wishlist = WishList.objects.filter(user__in=user)

    template = 'profiles/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)
    

@ login_required
def add_to_wishlist(request, item_id):
    """
    Adding a product to or removing a product
    from the wishlist
    """
    # print("ADD_TO_WISHLIST VIEW FIRED")

    product = Product.objects.get(pk=item_id)
    user = UserProfile.objects.get(user=request.user)
    redirect_url = request.POST.get('redirect_url')

    wishlist = WishList.objects.filter(product=product, user=user)

    if wishlist:
        wishlist.delete()
        messages.success(
            request, 'This product is removed from your wish list')
    else:
        list = WishList(product=product, user=user)
        list.save()
        messages.success(
            request, f'Added {product.name} to your wish list')
    if redirect_url:
        return redirect(redirect_url)
    else:
        return redirect('wishlist')


@ login_required
def review(request):
    """
    A view to show the review(s)
    """
    user = UserProfile.objects.filter(user=request.user)
    review = Review.objects.filter(user__in=user)

    template = 'products/product_detail.html'
    context = {
        'review': review
    }

    return render(request, template, context)


@ login_required
def add_review(request, item_id):
    """
    Adding a review
    """