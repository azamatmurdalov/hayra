from django.db import models

TITLE_CHOICES = (
	('Событийный волонтер', 'Событийный волонтер'),
	('Волонтер-донор', 'Волонтер-донор'),
	('Волонтер общественной безопасности', 'Волонтер общественной безопасности'),
	('Медиа-волонтер', 'Медиа-волонтер'),
	('Волонтер помощи страдающим паническими атаками', 'Волонтер помощи страдающим паническими атаками'),
	('Волонтеры финансовой помощи', 'Волонтеры финансовой помощи'),
)

class Volunteer(models.Model):
	name = models.CharField('Имя', max_length = 120)
	phone = models.CharField('Телефон', max_length = 120)
	role = models.CharField('Роль', max_length=120, choices=TITLE_CHOICES)
	date = models.DateTimeField('Дата добавления', auto_now_add = True)

	def __str__(self):
		return self.name