from importlib.resources import contents
from turtle import title
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# string to auth.user
# we are going to use the default user model


class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    # now here we will add user models as foreign key
    # on deleting user we would prefer to stay those bellow data as it is so we will allow null as well
    # default 1 will be the very first user which is the super user
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122"
