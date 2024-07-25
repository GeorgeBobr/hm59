from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from webapp.forms import IssueForm
from webapp.models import Issue, Project

class IssueDetailView(DetailView):
    template_name = "issue/issue_detail.html"
    model = Issue
    context_object_name = "issue"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = self.get_object()
        context['project'] = get_object_or_404(Project, id=issue.project.id)
        return context

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = "issue/issue_create.html"
    form_class = IssueForm

    def form_valid(self, form):
        form.instance.project = Project.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.get(pk=self.kwargs['pk'])
        return context

class IssueUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "issue/issue_update.html"
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse("webapp:issue_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = self.get_object()
        context['project'] = get_object_or_404(Project, id=issue.project.id)
        return context

class IssueDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "issue/issue_delete.html"
    model = Issue

    def get_success_url(self):
        return reverse("webapp:project_detail", kwargs={"pk": self.object.project.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = self.get_object()
        context['project'] = get_object_or_404(Project, id=issue.project.id)
        return context
