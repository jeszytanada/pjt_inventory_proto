from django import template
import datetime
from django.utils import formats

register = template.Library()

@register.filter
def get_format(value):
    if type(value) == datetime.datetime:
        return formats.date_format(value, 'SHORT_DATE_FORMAT')
    else:
        return value