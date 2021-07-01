from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=30)

class Images(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    posted = models.DateField(auto_now_add=True)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image(cls):
        image= cls.objects.get(pk=id)
        return image






