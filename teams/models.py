from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from configuration.models import Section, SectionTime


class Team(models.Model):
    # TODO: team number based on section
    members = models.ManyToManyField(User)
    availability = models.ManyToManyField(SectionTime)
    preferred_section = models.ForeignKey(Section, on_delete=models.CASCADE,
                                          related_name='preferred_section')
    assigned_section = models.ForeignKey(Section, on_delete=models.CASCADE, 
                                         related_name='assigned_section')

    def save(self, *args, **kwargs):
        # TODO: FIX ADMIN CRASH
        # this validates, but failed validation would just crash the admin panel

        # limit members to 2 or more
        # if (self.members.count() < 2):
        #     raise ValidationError('A team must have at least 2 members.')
        # # limit members to 5 or less
        # if (self.members.count() > 5):
        #     raise ValidationError('A team many only have up to 5 members.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Team {self.id}'
