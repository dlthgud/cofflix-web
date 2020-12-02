from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.name}'


class Cafe(models.Model):

    name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    open_time = models.TimeField(null=True)
    close_time = models.TimeField(null=True)
    holiday = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=50, null=True)
    tags = models.ManyToManyField(Tag)
    memo = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}: {self.address}: {self.open_time}: {self.close_time}: {self.holiday}: {self.tel}'

class Image(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='posts', null=True)
