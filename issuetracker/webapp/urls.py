from django.urls import path
from .views.views import IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView
from .views.project_views import (ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView,
                                  ProjectDeleteView)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    path('project/<int:pk>/issue/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('issue/update/<int:pk>/', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/delete/<int:pk>/', IssueDeleteView.as_view(), name='issue_delete'),
]
