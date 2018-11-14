from django.db import models

TITLE_CHOICES = (
	('Событийный волонтер', False),
	('Волонтер-донор', False),
	('Волонтер общественной безопасности', False),
	('Медиа-волонтер', False),
	('Волонтер помощи страдающим паническими атаками', False),
	('Волонтеры финансовой помощи', False),
)

class Volunteer(models.Model):
	name = models.CharField(max_length = 120)
	phone = models.CharField(max_length = 120)
	give = models.CharField(max_length=120, choices=TITLE_CHOICES)
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name