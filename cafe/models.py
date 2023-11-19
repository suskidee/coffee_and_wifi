from django.db import models
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _

# Define the choices for the fields
coffee_choices = [
    ('☕️', '☕️'),
    ('☕️☕️', '☕️☕️'),
    ('☕️☕️☕️', '☕️☕️☕️'),
    ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
    ('☕️☕️☕️☕️️☕️', '☕️☕️☕️☕️️☕️'),
    ('✘', '✘'),
]
wifi_choices = [
    ('💪️', '💪️'),
    ('💪️💪️', '💪️💪️'),
    ('💪️💪️💪️', '💪️💪️💪️'),
    ('💪️💪️💪️💪️', '💪️💪️💪️💪️'),
    ('💪️💪️💪️💪️💪️', '💪️💪️💪️💪️💪️'),
    ('✘', '✘'),
]
power_choices = [
    ('🔌', '🔌'),
    ('🔌🔌', '🔌🔌'),
    ('🔌🔌🔌', '🔌🔌🔌'),
    ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
    ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'),
    ('✘', '✘'),
]
open_choices = [
    ('5AM', '5AM'),
    ('6AM', '6AM'),
    ('7AM', '7AM'),
    ('8AM', '8AM'),
    ('9AM', '9AM'),
    ('10AM', '10AM'),
]
close_choices = [
    ('5PM', '5PM'),
    ('6PM', '6PM'),
    ('7PM', '7PM'),
    ('8PM', '8PM'),
    ('9PM', '9PM'),
    ('10PM', '10PM'),
]


# Create the model class
class Cafe(models.Model):
    # Define the fields of the model
    cafe = models.CharField(_('cafe name'), max_length=100)
    city = models.CharField(_('city'), max_length=100)
    location = models.URLField(_('location url'), validators=[URLValidator])
    open = models.CharField(_('open'), max_length=4, choices=open_choices, default='9AM')
    close = models.CharField(_('close'), max_length=4, choices=close_choices, default='5PM')
    coffee = models.CharField(_('coffee rating'), max_length=11, choices=coffee_choices, default='☕️')
    wifi = models.CharField(_('wifi rating'), max_length=10, choices=wifi_choices, default='💪️')
    power = models.CharField(_('power outlet rating'), max_length=5, choices=power_choices, default='🔌')

    # Define the string representation of the model
    def __str__(self):
        return self.cafe
