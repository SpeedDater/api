from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from random import randint
from configuration.models import Section, SectionTime
from speeddater_api.helpers import num_digits, first_n_digits


class Team(models.Model):
    number = models.SmallIntegerField(verbose_name='Team number')
    member1 = models.OneToOneField(User, on_delete=models.CASCADE,
                                   related_name='member1', blank=True, null=True)
    member2 = models.OneToOneField(User, on_delete=models.CASCADE,
                                   related_name='member2', blank=True, null=True)
    member3 = models.OneToOneField(User, on_delete=models.CASCADE,
                                   related_name='member3', blank=True, null=True)
    member4 = models.OneToOneField(User, on_delete=models.CASCADE,
                                   related_name='member4', blank=True, null=True)
    member5 = models.OneToOneField(User, on_delete=models.CASCADE,
                                   related_name='member5', blank=True, null=True)
    availability = models.ManyToManyField(SectionTime)
    preferred_section = models.ForeignKey(Section, on_delete=models.CASCADE,
                                          related_name='preferred_section')
    assigned_section = models.ForeignKey(Section, on_delete=models.CASCADE,
                                         null=True, blank=True,
                                         related_name='assigned_section')

    def count_members(self):
        # team is not full
        if None in members_set:
            return len(members) - 1
        else:
            return len(members)

    def clean(self):
        count = 0
        members = [self.member1, self.member2,
                   self.member3, self.member4, self.member5]
        members_set = set(members)

        # count members in list
        for m in members:
            if m:
                count += 1
        # count members in set (subtract one if there are null values)
        set_count = (len(members_set) - 1) if None in members_set \
            else len(members_set)

        # if two counts are different, there are duplicates
        if count != set_count:
            raise ValidationError('Teams must not have duplicate members.')
        # check min/max count
        if count < 2:
            raise ValidationError('Teams must have at least 2 members.')
        elif count > 5:
            raise ValidationError('Teams may only have up to 5 members')

    def save(self, *args, **kwargs):
        # validate team
        self.clean()
        # haxx: save with random number if there's no PK
        if not self.id:
            self.number = randint(-30000, -1)
            super().save(*args, **kwargs)

        # change Team Number to section + # in section (ex. 407)
        # only assign number if team is assigned to section, and the first digits
        # of team number doesn't match with section number
        if self.assigned_section:
            assigned_section_num = self.assigned_section.number
            section_in_team_num = first_n_digits(assigned_section_num,
                                                 num_digits(assigned_section_num))
            if assigned_section_num != section_in_team_num:
                num_in_section = Team.objects.filter(
                    assigned_section=self.assigned_section).count() + 1
                num_in_section = str(num_in_section).zfill(2)
                self.number = int(f'{self.assigned_section}{num_in_section}')
        # invalidate Team Number if team becomes unassigned
        elif not self.assigned_section:
            self.number = -1 * self.id

        # save again with new team number
        super().save(*args, **kwargs)

    def __str__(self):
        if self.number > 0:
            return f'Team {self.number}'
        else:
            return f'** UNASSIGNED #{self.id}'
