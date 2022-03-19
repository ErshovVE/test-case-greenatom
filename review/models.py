from django.db import models

# Create your models here.

class Review(models.Model):
    review_text = models.CharField(max_length=1000)
    review_class = models.BooleanField()
    review_stars = models.IntegerField()
    def __str__(self):
        return self.review_text