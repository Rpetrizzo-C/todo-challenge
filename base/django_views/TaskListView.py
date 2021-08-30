from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from ..models import Task
from ..forms import PositionForm

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area', '')
        order_complete  = self.request.GET.get('order-complete', '')
        order_last_first  = self.request.GET.get('order-created', '')
        order_last  = self.request.GET.get('order--created', '')

        if order_last_first:
            context['tasks'] = context['tasks'].filter(user=self.request.user).order_by('created')

        if order_last:
            context['tasks'] = context['tasks'].filter(user=self.request.user).order_by('-created')

        if order_complete:
            context['tasks'] = context['tasks'].filter(user=self.request.user).order_by('complete')
            
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context