from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm, SearchForm
from webapp.models import Project, Issue

class ProjectListView(ListView):
    model = Project
    template_name = "project/project_list.html"
    ordering = ['-start_data']
    context_object_name = "projects"
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context


class ProjectDetailView(DetailView):
    template_name = "project/project_detail.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issues"] = Issue.objects.filter(project=self.object)
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "project/project_create.html"
    form_class = ProjectForm
    success_url = reverse_lazy('webapp:project_list')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "project/project_update.html"
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse_lazy('webapp:project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "project/project_delete.html"
    model = Project
    success_url = reverse_lazy('webapp:project_list')
