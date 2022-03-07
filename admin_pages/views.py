from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, RedirectView
from configuration.forms import *
from configuration.models import *


class AdminLogoutRedirectView(RedirectView):
    query_string = True
    pattern_name = 'account_logout'


@method_decorator(staff_member_required(), name='dispatch')
class MajorBulkUpdateView(FormView):
    '''
    Bulk import majors from the Admin Panel
    '''
    form_class = BulkUpdateForm
    success_url = reverse_lazy('admin:configuration_major_changelist')
    template_name = 'bulk_import_majors.html'
    extra_context = {
        'title': 'Bulk import majors',
        'site_header': settings.APP_NAME,
        # TODO: why are buttons on the top-right (view site, log out, etc) missing?
    }

    def form_valid(self, form):
        # load input per line
        majors = form.cleaned_data['content'].split('\r\n')
        # build objects list, bulk create in db, ignore non-unique objects
        objs = [Major(major=m) for m in majors]
        Major.objects.bulk_create(objs, ignore_conflicts=True)
        return super().form_valid(form)


@method_decorator(staff_member_required(), name='dispatch')
class SkillBulkUpdateView(FormView):
    '''
    Bulk import skills from the Admin Panel
    '''
    form_class = BulkUpdateForm
    success_url = reverse_lazy('admin:configuration_skill_changelist')
    template_name = 'bulk_import_skills.html'
    extra_context = {
        'title': 'Bulk import skills',
        'site_header': settings.APP_NAME,
        # TODO: why are buttons on the top-right (view site, log out, etc) missing?
    }

    def form_valid(self, form):
        # load input per line
        skills = form.cleaned_data['content'].split('\r\n')
        # build objects list, bulk create in db, ignore non-unique objects
        objs = [Skill(skill=s) for s in skills]
        Skill.objects.bulk_create(objs, ignore_conflicts=True)
        return super().form_valid(form)
