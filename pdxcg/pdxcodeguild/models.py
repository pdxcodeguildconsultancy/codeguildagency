from django.db import models
from django.core.validators import RegexValidator


class NewStudentApplication(models.Model):
    # regex for valid international phone number
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits \
                                 allowed.")

    first_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now=False)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField(max_length=5)
    applied_before = models.BooleanField()
    if_yes_app = models.DateField(auto_now=False)
    attended_before = models.BooleanField()
    if_yes_grad = models.CharField(max_length=255)
    if_no_grad = models.TextField(max_length=255)
    phone_number = models.CharField(validators=[phone_regex], blank=True)
    message_number = models.CharField(validators=[phone_regex], blank=True)
    cell_number = models.CharField(validators=[phone_regex], blank=True)
    email = models.EmailField()
    us_citizen = models.BooleanField()

    # Emergency Contact Information

    contact_name = models.CharField(max_length=255)
    contact_address = models.CharField(max_length=255)
    contact_city = models.CharField(max_length=255)
    contact_state = models.CharField(max_length=255)
    contact_zip = models.CharField(max_length=255)
    contact_number = models.CharField(validators=[phone_regex], blank=True)