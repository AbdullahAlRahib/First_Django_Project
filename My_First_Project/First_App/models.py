from platform import release
from django.db import models

# Create your models here.
class Musicians(models.Model):
    #id = models.AutoField(Primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+" "+self.last_name+" played "+self.instrument+""

class Album(models.Model):
    #id = models.AutoField(Primary_key=True) if we use CASCADE
    artist = models.ForeignKey(Musicians, on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    release_date = models.DateField()
    rating = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Best"),
    )
    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return self.name+" got "+str(self.num_stars)+" stars "