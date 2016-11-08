from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import re

# Create your models here.
@python_2_unicode_compatible
class Mentor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def clean(self):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", self.email):
            raise Exception("not a valid e-mail address")

    def __str__(self):
        return self.first_name + " " + self.last_name

@python_2_unicode_compatible
class Opinion(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
