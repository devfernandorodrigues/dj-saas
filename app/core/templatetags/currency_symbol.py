from babel.numbers import get_currency_symbol
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def currency_symbol(value):
    return get_currency_symbol(value.upper())


@register.filter
def currency_divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return None
