from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=20) #oopss :)  #we can extend length :)
    task_desc = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    by_person = models.ForeignKey('auth.User', related_name='TaskApp', on_delete=models.CASCADE)

    def __str__(self):
        return  "%s" % self.task_name
class User(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.CharField(max_length=100)
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)

	def __str__(self):
		return "%s" % self.username
    
