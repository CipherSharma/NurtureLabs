from django.db.models import AutoField
from django.db import models

# Create your models here.
def upload_to(instance,filename):
    return '/(filename)',format(filename=filename)

class Advisor(models.Model):
    AdvisorName=models.CharField(max_length=122,null=True)
    AdvisorImage=models.ImageField(upload_to=upload_to,default='default.jpg')

    def __str__ (self):
        return self.AdvisorName

class Bookings(models.Model):
    AdvisorId = models.ForeignKey(Advisor, on_delete=models.CASCADE,default='0')
    UserId = models.IntegerField(null=True,blank=True)
    BookingTime=models.DateTimeField("%y-%m-%d %H:%M:%S",null=True,blank=True)
