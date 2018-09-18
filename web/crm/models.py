from django.db import models
from django.utils import timezone

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    primary_phone = models.CharField(max_length=10)
    secondary_phone = models.CharField(max_length=10, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Note(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content[:10]

