from django.db import models

class Volunteer(models.Model):
	name = models.CharField(max_length = 120)
	phone = models.CharField(max_length = 120)
	give = models.TextField()
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name