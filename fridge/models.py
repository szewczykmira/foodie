from django.db import models

class Food(models.Model):
    since_when = models.DateTimeField(_("Since when"), auto_now=False, auto_now_add=False)
    expiration_date = models.DateTimeField(_("Expiration date"), auto_now=False, auto_now_add=False)
    name = models.TextField(_("Name"))
    quantity = models.TextField(_("Quantity"), blank=True)