from django.db import models

# Creation of class.
class DjangoClasses(models.Model):
    title = models.CharField(max_length=100)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=60)
    duration = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)

    # The models.Manager() is the interface through which dB query operations are provided to Django models.
    objects = models.Manager()

    # Called whenever str() is called on an object. Used to display an object in the Django admin site.
    def __str__(self):
        return self.title



