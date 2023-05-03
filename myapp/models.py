from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Product(models.Model):
    name = models.CharField(_("Product Name"), max_length=50)
    qunatity = models.IntegerField(_("Quantity"))
    create_date = models.DateField(_("Created Date"),auto_now_add=True)
    manufacture_place = models.CharField(_("Manufacture Place"), max_length=50)