"""
Views of the profiles app
"""
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from products.models import Product
from .forms import ReviewForm

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

    template = 'profiles/review.html'
    context = {
        'reviews': reviews
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id):
    """ Add a review to a product """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES) # 2nd to capture image
        if form.is_valid():
            review = form.save()
            review.user = user
            review.product = product
            review.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add review.'
                'Please ensure the form is valid.')
    else:
        user = get_object_or_404(UserProfile, user=request.user)
        product = get_object_or_404(Product, pk=product_id)
        # initial = {'product': product,
        #             'user': user 
        #         }
        form = ReviewForm()
    
    template = 'profiles/add_review.html'
    context = {
        'form': form,
        'from_product_detail': True,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ Edit a product in the store """

    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('review'))
        else:
            messages.error(request,
                           'Failed to update review.'
                           'Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, 'You are editing this review')

    template = 'profiles/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('review'))


# @ login_required
# def add_review(request, item_id):
#     """
#     Adding or removing a review
#     """
#     product = Product.objects.get(pk=item_id)
#     user = UserProfile.objects.get(user=request.user)
#     redirect_url = request.POST.get('redirect_url')

#     all_reviews = Review.objects.filter(product=product, user=user)

#     if all_reviews:
#         all_reviews.delete()
#         messages.success(
#             request, 'This review is removed from your reviews')
#     else:
#         r_list = Review(product=product, user=user)
#         r_list.save()
#         messages.success(
#             request, 'Added review to your reviews')
#     if redirect_url:
#         return redirect(redirect_url)
#     else:
#         return redirect('review')
