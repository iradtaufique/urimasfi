from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_member = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)



class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_Name = models.CharField(max_length=80)
    last_Name = models.CharField(max_length=80)
    email = models.EmailField()
    image = models.ImageField(upload_to='profile')



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transport(models.Model):
    transport = models.CharField(max_length=50)

    def __str__(self):
        return self.transport


class Report(models.Model):
    note = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()

    def __str__(self):
        return self.owner



STATUS = (
    ('Aproved', 'APROVED'),
    ('Rejected', 'REJECTED'),
    ('Pending', 'PENDING'),
    ('Autholized', 'AUTHOLIZED'),
)


class Mission(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='missions')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='missions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    mission_purpose = models.CharField(max_length=100)
    mission_result = models.CharField(max_length=100)
    mission_destination = models.CharField(max_length=100)
    distance = models.CharField(max_length=20)
    departure_date = models.DateField()
    returning_date = models.DateField()
    mission_duration = models.CharField(max_length=50)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    invitation = models.FileField(upload_to='doc_file')




class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    missions = models.ManyToManyField(Mission)
    school = models.ManyToManyField(School)

    # def __str__(self):
    #     return self.user