from django.db import models
from django.urls import reverse

# Create your models here.
class Phone(models.Model):
    RAM_CAPACITY = (
        ('3', '3'),
        ('4', '4'),
        ('6', '6'),
        ('8', '8'),
        ('12', '12'),
    )

    ROM_CAPACITY= (
        ('32', '32'),
        ('64', '64'),
        ('128', '128'),
        ('264', '264'),
        ('512', '512'),
        ('1024', '1024')
        )
    brand_name = models.CharField(max_length=64)
    model_name = models.CharField(max_length=64)
    color = models.ForeignKey("Color", on_delete=models.SET_NULL, null=True)
    battery = models.SmallIntegerField(default=0, help_text="mAh")
    price = models.SmallIntegerField(default=0, help_text="AZN")
    ram = models.CharField(max_length=2, choices=RAM_CAPACITY)
    memory = models.CharField(max_length=4, choices=ROM_CAPACITY, help_text="GB")
    is_new = models.BooleanField(default=False)
    fingerprint = models.BooleanField(default=False)
    fice_id = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos/phones/%Y/%m/%d/")
    description = models.TextField(max_length=3000, null=True)
    
    def __str__(self) -> str:
        return f"{self.brand_name}"
    
    def get_absolute_url(self) -> str:
        return reverse("details", kwargs={'pk':self.pk})

    
class Color(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self) -> str:
        return f"{self.name}"

