from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='department', blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'
    def __str__(self):
        return '{}'.format(self.name)
    def get_url(self):
        return reverse('schoolapp:courses_by_department',args=[self.slug])
class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    seats = models.IntegerField()
    image = models.ImageField(upload_to='pics', blank=True)




    class Meta:
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('schoolapp:coursedetail', args=[self.department.slug,self.slug])
