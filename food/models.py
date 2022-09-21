from django.db import models

# Create your models here.
category = (
    ("1","starter"),
    ("2","soup"),
    ("3","main"),
    ("4","pizza"),
    ("5","hamburger"),
    ("6","dessert"),
    ("7","wine"),
    ("8","beer"),
)

class Food(models.Model):
    f_id = models.IntegerField(blank=False,null=False,unique=True)
    name = models.CharField(max_length=60,blank=False,null=False,unique=True)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    category = models.CharField(choices=category,max_length=2,blank=False,null=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['category','name']

    def get_available_food(self):
        return self.objects.filter(is_active=True)


    def __str__(self):
        return "["+str(self.category) +"] " + self.name

