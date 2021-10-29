"""
Create and register a template filter
"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """function to calculate the subtotal"""
    return price * quantity
