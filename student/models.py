from django.db import models

## function to handle the location of resumes.
def upload_status_image(instance , filename):
    return "student/{user}/{filename}".format(user=instance.companyname , filename=filename)

# Create your models here.
class StudentLogin(models.Model):

    ## all fields for Student registration table.
    fullname = models.CharField(max_length=256, blank=False, null=False)
    course = models.CharField(max_length=256, blank=False, null=False)
    semester = models.IntegerField()
    department = models.CharField(max_length=256, blank=False, null=False)
    email = models.CharField(max_length=256)
    mobno = models.BigIntegerField()
    password = models.CharField(max_length=256)

    ## Method to display full name instead of object name.
    def __str__(self):
        return self.fullname

class StudentApplicationForm(models.Model):

    ## all fields for Student Application form.
    email = models.CharField(max_length=256)
    companyname = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    reason = models.TextField()
    resume = models.FileField(null=True, upload_to=upload_status_image)
    datetimestamp = models.DateTimeField(auto_now_add=True,null=True)
    status = models.IntegerField(default=1)

    ## Method to display email instead of object name.
    def __str__(self):
        return self.email

class TPO(models.Model):

    ## all fields for TPO registration
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256, null=False)
    password = models.CharField(max_length=32, null=False)

    ## Method to display name instead of object name.
    def __str__(self):
        return self.name