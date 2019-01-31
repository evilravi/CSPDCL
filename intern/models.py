from django.db import models
from django.core.urlresolvers import reverse



class Courses(models.Model):
    Course = models.CharField(max_length= 100,primary_key= True)
    images = models.FileField(default='')

    def __str__(self):
        return self.Course


class Batch(models.Model):
    Course = models.ManyToManyField(Courses)
    Batch_No = models.CharField(max_length= 30,primary_key=True)

    def __str__(self):
        return self.Batch_No


class Person(models.Model):
    Rack_No = models.CharField(max_length=1000, null=True)
    File_No = models.CharField(max_length=1000, null=True)
    Order_No = models.CharField(max_length=1000, null=True)
    Document_No = models.CharField(max_length=1000, null=True)
    Course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    Batch_No = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=100 , null= True)
    Father_Name = models.CharField(max_length=100, null= True)
    Date_of_Order_Issue = models.DateField(null= True , blank = True)
    Date_of_Joining = models.DateField(null=True, blank=True)
    Date_of_Ending = models.DateField(null=True, blank=True)
    Name_of_Division = models.CharField(max_length=100, null= True)


    def __str__(self):
        return self.Name


class Image(models.Model):
    Course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    image = models.FileField(default='')

    def __str__(self):
        return self.Course.Course


class Contact(models.Model):
    Course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=100, null=True)
    Image = models.FileField(default='')
    Designation = models.CharField(max_length=100, null=True)
    Contact_No = models.CharField(max_length=100, null=True)
    Email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Name
