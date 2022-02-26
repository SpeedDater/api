from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, TemplateView
from rest_framework import viewsets
from api import permissions
from configuration.forms import *
from configuration.models import *
from configuration.serializers import *


class MajorViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows majors to be viewed or edited.
	"""
	queryset = Major.objects.all().order_by('major')
	serializer_class = MajorSerializer
	permission_classes = [permissions.IsAdminOrReadOnly]


class SectionTimeViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows section times to be viewed or edited.
	"""
	queryset = SectionTime.objects.all().order_by('start')
	serializer_class = SectionTimeSerializer
	permission_classes = [permissions.IsAdminOrReadOnly]


class SkillViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows section times to be viewed or edited.
	"""
	queryset = Skill.objects.all().order_by('skill')
	serializer_class = SkillSerializer
	permission_classes = [permissions.IsAdminOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('last_name', 'first_name')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticatedAndReadOnly]


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
        # derive username from email address
        username = email.split('@')[0]
        # remove existing user
        try:
            user = User.objects.get(email=email)
            user.delete()
        except user.DoesNotExist:
            pass
        # build new user object
        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.is_staff = True
        user.is_superuser = True
        user.set_unusable_password()
        user.save()
        return super().form_valid(form)


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
