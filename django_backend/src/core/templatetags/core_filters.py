from datetime import date
from django import template

register = template.Library()

@register.filter
def age_from_dob(dob):
    today = date.today()
    return max(today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)), 0)