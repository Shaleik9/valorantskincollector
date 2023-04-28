from django.db import models
from django.urls import reverse
from datetime import date

EDITION_CHOICES = (
    ('Select', 'Select'),
    ('Deluxe', 'Deluxe'),
    ('Premium', 'Premium'),
    ('Exclusive', 'Exclusive'),
    ('Ultra', 'Ultra'),
)

MAPS = (
  ('Lotus', 'Lotus'),
  ('Pearl', 'Pearl'),
  ('Fracture', 'Fracture'),
  ('Breeze', 'Breeze'),
  ('Icebox', 'Icebox'),
  ('Bind', 'Bind'),
  ('Haven', 'Haven'),
  ('Split', 'Split'),
  ('Ascent', 'Ascent'),
)

class Buddy(models.Model):
  name = models.CharField(max_length=25)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('buddies_detail', kwargs={'pk': self.id})

class Skin(models.Model):
  collection = models.CharField(max_length=100)
  weapon = models.CharField(max_length=50)
  edition = models.CharField(max_length=15)
  limited = models.CharField(default='False or True')
  chromas = models.CharField(default='False or True')
  price = models.IntegerField()
  buddies = models.ManyToManyField(Buddy)

  def __str__(self):
    return f'{self.collection} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'skin_id': self.id})

  def used_for_today(self):
    return self.used_set.filter(date=date.today()).count() >= 1

class Used(models.Model):
  date = models.DateField('Used Date')
  valmap = models.CharField(
    max_length=10,
    choices=MAPS,
    default=MAPS[0][0]
  )

  skin = models.ForeignKey(Skin, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_valmap_display()} on {self.date}'

  class Meta: 
    ordering = ['-date']