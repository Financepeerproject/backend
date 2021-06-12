from django.db import models

# Create your models here.
class UploadedData(models.Model):
    userId = models.IntegerField(unique=True, null=False)
    id = models.IntegerField(unique=True, null=False, primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return str(self.userId)+"-"+str(self.id)+"-"+self.title

