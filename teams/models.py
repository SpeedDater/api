from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from configuration.models import Section, SectionTime


class Team(models.Model):
    number = models.SmallIntegerField(null=True, verbose_name='Team number')
    members = models.ManyToManyField(User)
    availability = models.ManyToManyField(SectionTime)
    preferred_section = models.ForeignKey(Section, on_delete=models.CASCADE,
                                          related_name='preferred_section')
    assigned_section = models.ForeignKey(Section, on_delete=models.CASCADE,
                                         null=True, blank=True,
                                         related_name='assigned_section')

    def save(self, *args, **kwargs):
        # TODO: FIX ADMIN CRASH
        # this validates, but failed validation would just crash the admin panel

        # limit members to 2 or more
        if (self.members.count() < 2):
            raise ValidationError('A team must have at least 2 members.')
        # limit members to 5 or less
        if (self.members.count() > 5):
            raise ValidationError('A team many only have up to 5 members.')

        # change Team ID to section + # in section (ex. 407)
        # only assign number if team is assigned to section and there isn't a number yet
        if self.assigned_section and not self.number:
            num_in_section = Team.objects.filter(
                assigned_section=self.assigned_section).count() + 1
            num_in_section = str(num_in_section).zfill(2)
            self.number = int(f'{self.assigned_section}{num_in_section}')
        super().save(*args, **kwargs)

    def __str__(self):
        if self.number:
            return f'Team {self.number}'
        else:
            return f'** Unassigned #{self.id} **'
