from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from configuration import models as config_models


# main user profile for speed dating
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)
    phone = models.CharField(max_length=10, blank=True, default='',
                             validators=[MinLengthValidator(10)],
                             verbose_name='Phone number',
                             help_text='Enter 10 digits, without any special characters')
    availability = models.ManyToManyField(config_models.SectionTime,
                                          blank=False)
    majors = models.ManyToManyField(config_models.Major, blank=False)
    interests = models.ManyToManyField(config_models.Skill,
                                       blank=False, related_name='interests')
    skills = models.ManyToManyField(config_models.Skill,
                                    blank=False, related_name='skills')
    looking_for = models.TextField(blank=False)
    anything_else = models.TextField(blank=False)

    def full_name(self):
        return self.user.get_full_name()

    def email(self):
        return self.user.email

    def __str__(self):
        return self.user.username
