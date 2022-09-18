from cgitb import lookup
from importlib.resources import contents
from turtle import title
from django.db import models
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL

# we will create first product query set so that we can use it on ProductManager


class ProductQuerySet(models.QuerySet):
    # here we can implement query that we are try to do so that we can use these queryset on other query
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        # now here we will implement search feature
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        # here this look up will look into 'title' and 'content' field in the Product
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    # now we will override the default queryset
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)
        # here we are passing same model and default database

    def search(self, query, user=None):
        # now here we will return the product that user try to search by filtering it
        # return Product.objects.filter(public=True).filter(title_icontains=query)

        # now we had defined 'ProductQuerySet' we can use that here
        # return self.get_queryset().filter(public=True).filter(title_icontains=query)
        # get_queryset() is that function build into the model that refer to the 'ProductQuerySet' methods

        # because we have override the default 'get_queryset' now rather we can do this and add 'is_public()' function & 'search()' function
        return self.get_queryset().is_public().search(query, user=user)
        # we had added 'is_public' function on 'search' function so need to add it in here


class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    # we will add new two field here
    public = models.BooleanField(default=True)
    objects = ProductManager()

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122"
