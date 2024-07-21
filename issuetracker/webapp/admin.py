from django.contrib import admin
from webapp.models import Issue, Status, Type, Project

admin.site.register(Project)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Issue)
