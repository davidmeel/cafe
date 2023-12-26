from django.db import models

# Create your models here.


class Mode(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to="image")
    info = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    




class ReservationModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'




class MenuModel(models.Model):
    title = models.CharField(max_length=64)
    info = models.CharField(max_length=255)
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'