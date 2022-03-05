from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, RedirectView
from configuration.forms import *
from configuration.models import *


def add_admin_context(context):
    context['site_header'] = settings.APP_NAME
    context['site_url'] = '/'
    context['has_permission'] = True


class AdminLogoutRedirectView(RedirectView):
    query_string = True
    pattern_name = 'account_logout'


@method_decorator(staff_member_required(), name='dispatch')
class MajorBulkUpdateView(FormView):
    """
    A view for admins to bulk import majors.
    """
    form_class = BulkUpdateForm
    success_url = reverse_lazy('admin:configuration_major_changelist')
    template_name = 'bulk_import_majors.html'

    def form_valid(self, form):
        # load input per line
        majors = form.cleaned_data['content'].split('\r\n')
        # build objects list, bulk create in db, ignore non-unique objects
        objs = [Major(major=m) for m in majors]
        Major.objects.bulk_create(objs, ignore_conflicts=True)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bulk import majors'
        add_admin_context(context)
        return context


@method_decorator(staff_member_required(), name='dispatch')
class SkillBulkUpdateView(FormView):
    """
    A view for admins to bulk import skills.
    """
    form_class = BulkUpdateForm
    success_url = reverse_lazy('admin:configuration_skill_changelist')
    template_name = 'bulk_import_skills.html'

    def form_valid(self, form):
        # load input per line
        skills = form.cleaned_data['content'].split('\r\n')
        # build objects list, bulk create in db, ignore non-unique objects
        objs = [Skill(skill=s) for s in skills]
        Skill.objects.bulk_create(objs, ignore_conflicts=True)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bulk import skills'
        add_admin_context(context)
        return context
