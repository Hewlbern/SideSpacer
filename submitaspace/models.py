from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

# Create your models here.

class PlaceOwner(models.Model):
    TYPE_OF_LOCATION = (
        (0, 'Restaurant'), (1, "Bar"), (2, "Office"),
        (3, "Hotel"), (4, "Other"),
    )
    type_of_location = models.IntegerField(verbose_name= "What type of location is it?", default= 0, choices = TYPE_OF_LOCATION )

    LOCATION = (
        ('Melbourne', 'Melbourne'),
        ('Sydney', 'Sydney'),
        ('Canberra', 'Canberra'),
    )

    location  = models.CharField(verbose_name="In which city is your location?", max_length=200, default='', choices= LOCATION )

    nameofthelocation    = models.CharField(verbose_name="What is the name of the Location?", max_length=120, default='')

    websiteurl    = models.URLField(verbose_name="What is the Website URL?", blank='True', null='True')

    address    = models.CharField(verbose_name="What is the Street Address?", max_length=120, default='')

    seatingcapacity    = models.CharField(verbose_name="What is the seating capacity?", max_length=120, default='')

    THE_TIME = (
        ('4:00pm', '4:00pm'),
        ('4:30pm', '4:30pm'),
        ('5:00pm', '5:00pm'),
        ('5:30pm', '5:30pm'),
        ('6:00pm', '6:00pm'),
        ('6:30pm', '6:30pm'),
    )

    thetime  = models.CharField(verbose_name="At what time does dinner typically start?", max_length=200, default='', choices= THE_TIME )

    THE_DAYS = (
        ('7 Days a Week', '7 Days a Week'),
        ('Weekdays only', 'Weekdays only'),
        ('Weekends only', 'Weekends only'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    thedays  = models.CharField(verbose_name="Which days would you like Spacious to operate in your space?", max_length=200, default='', choices= THE_DAYS )

    name = models.CharField(verbose_name="Your First name", max_length=120, default='')

    lastname = models.CharField(verbose_name="Your Last name", max_length=120, default='')

    phone_number = PhoneNumberField(verbose_name="Your Phone number", default='')

    email   = models.EmailField(max_length=120, default='')

    THE_WAYS = (
    ('E-mail', 'E-mail'),
    ('Phone', 'Phone'),
    ('Text', 'Text'),
    )

    theways = MultiSelectField(verbose_name="What's the best way to reach you?", default='', choices= THE_WAYS)

    def __str__(self):
        return 'Name: {}, E-mail:{}'.format(self.name, self.email)
