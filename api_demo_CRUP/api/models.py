from django.db import models
# Create your models here.
class HocTap(models.Model):
    MSSV = models.CharField(max_length=10)
    HOTEN = models.CharField(max_length=50)
    LOP= models.CharField(max_length=50)
    SDT = models.IntegerField(max_length=10)

    def __str__(self):
        return self.MSSV