"""
Views of the profiles app
"""
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    w_list = WishList.objects.filter(user__in=user)

    template = 'profiles/wishlist.html'
    context = {
        'wishlist': w_list,
    }

    return render(request, template, context)


@ login_required
def add_to_wishlist(request, item_id):
    """
    Adding or removing a product to or
    from the wishlist
    """
    product = Product.objects.get(pk=item_id)
    user = UserProfile.objects.get(user=request.user)
    redirect_url = request.POST.get('redirect_url')

    all_wishlist = WishList.objects.filter(product=product, user=user)

    if all_wishlist:
        all_wishlist.delete()
        messages.success(
            request, 'This product is removed from your wish list')
    else:
        w_list = WishList(product=product, user=user)
        w_list.save()
        messages.success(
            request, f'Added {product.name} to your wish list')
    if redirect_url:
        return redirect(redirect_url)
    else:
        return redirect('wishlist')


@ login_required
def review(request):
    """
    A view to show the review(s) of a user
    """
    user = UserProfile.objects.filter(user=request.user)
    reviews = Review.objects.filter(user__in=user)

    template = 'products/product_detail.html'
    context = {
        'reviews': reviews
    }
    print(reviews)
    return render(request, template, context)


@ login_required
def add_review(request, item_id):
    """
    Adding or removing a review
    """
    product = Product.objects.get(pk=item_id)
    user = UserProfile.objects.get(user=request.user)
    redirect_url = request.POST.get('redirect_url')

    all_reviews = Review.objects.filter(product=product, user=user)

    if all_reviews:
        all_reviews.delete()
        messages.success(
            request, 'This review is removed from your reviews')
    else:
        r_list = Review(product=product, user=user)
        r_list.save()
        messages.success(
            request, f'Added this review to your reviews')
    if redirect_url:
        return redirect(redirect_url)
    else:
        return redirect('review')
