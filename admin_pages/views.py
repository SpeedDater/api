from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from configuration.forms import *
from configuration.models import *


def add_admin_context(context):
    context['site_header'] = settings.APP_NAME
    context['site_url'] = '/'
    context['has_permission'] = True


@method_decorator(staff_member_required(), name='dispatch')
class AddStaffView(FormView):
    "A view for admins to add staff user accounts."
    form_class = AddStaffForm
    success_url = reverse_lazy('admin:auth_user_changelist')
    template_name = 'add_staff.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']

        # check for existing user with same email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User()

        # build user object
        user.username = email
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add staff account'
        add_admin_context(context)
        return context


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
