
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Task


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

