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


@login_required()
def wishlist(request):
    """View to show wishlist page"""
    return render(request, 'profiles/wishlist.html')


# @ login_required
# def wishlist(request):
#     """
#     A view to show the wishlist
#     """
#     try:
#         user = UserProfile.objects.filter(user=request.user)
#         product = Product.objects
#         w_list = WishList.objects.all()

#         template = 'profiles/wishlist.html'
#         context = {
#             'user': user,
#             'product': product,
#         }

#         return render(request, template, context)
#     except wishlist.DoesNotExist:

#         template = 'profiles/wishlist.html'
#         context = {
#             'error': 'No wishlist found.'
#         }
#         return render(request, template, context)


@ login_required
def add_to_wishlist(request, item_id):
    """
    Adding a product to the wishlist
    """
    print("ADD_TO_WISHLIST VIEW FIRED")

    product = Product.objects.get(pk=item_id)
    user = get_object_or_404(UserProfile, user=request.user)
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in wishlist:
        wishlist.pop(item_id)
        messages.error(
            request, 'This product is already in your Wish List')
    else:
        wishlist.append(item_id)
        messages.success(
            request, f'Added {product.name} to your wish list')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)

    # if  product in wishlist:
    #     product.remove(request.user)
    #     messages.error(
    #         request, 'This product is already in your Wish List')
    # else:
    #     product.add(request.user)
    #     messages.success(
    #         request, f'{ product.name} was added to your Wish List')
    #     return HttpResponseRedirect(request.META["HTTP_REFERER"])


@ login_required
def remove_from_wishlist(request, item_id):
    """
    Delete a product from the wishlist
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        wishlist = request.session.get('wishlist', {})

        if not request.user.is_logged_in(user=request.user.id):
            messages.error(
            request, 'Sorry, only logged in account users can do that.')
            return redirect(reverse('home'))
        else:
            wishlist.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your wish list')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
