from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


# available majors/minors
class Major(models.Model):
    major = models.CharField(max_length=50, blank=False, unique=True, default='')

    def __str__(self):
        return self.major


# available interests/skills
class Skill(models.Model):
    skill = models.CharField(max_length=50, blank=False, unique=True, default='')

    def __str__(self):
        return self.skill


# choice of discussion section times
class SectionTime(models.Model):
    start = models.TimeField(blank=False, unique=True)
    end = models.TimeField(blank=False, unique=True)

    def __str__(self):
        return f'{self.start} - {self.end}'
