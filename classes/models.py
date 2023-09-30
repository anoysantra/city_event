from django.db import models
# Create your models here.

class Classes(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name


class Section(models.Model):
    class_name=models.CharField(max_length=100)
    section_name=models.CharField(max_length=100)

    def __str__(self):
        return self.section_name


