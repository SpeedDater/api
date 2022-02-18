from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, TemplateView
from rest_framework import viewsets
from api import permissions
from configuration.forms import BulkUpdateForm
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
class BulkUpdateView(TemplateView):
    """
    A view for admins to bulk import majors.
    """
    template_name = 'bulk_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BulkUpdateForm()
        return context


@method_decorator(staff_member_required(), name='dispatch')
class MajorBulkUpdateView(FormView):
    """
    A view for admins to bulk import majors.
    """
    form_class = BulkUpdateForm
    success_url = reverse_lazy('bulk_update')

    def get(self, request):
        return HttpResponseNotAllowed(['POST'])

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
    success_url = reverse_lazy('bulk_update')

    def get(self, request):
        return HttpResponseNotAllowed(['POST'])

    def form_valid(self, form):
        # load input per line
        skills = form.cleaned_data['content'].split('\r\n')
        # build objects list, bulk create in db, ignore non-unique objects
        objs = [Skill(skill=s) for s in skills]
        Skill.objects.bulk_create(objs, ignore_conflicts=True)
        return super().form_valid(form)
