from django.contrib import admin
from .models import Project, ProjectCategory, Practice, Positionpractice

class ProjectCategoryAdmin(admin.ModelAdmin):
    model = ProjectCategory

class ProjectAdmin(admin.ModelAdmin):
    model = Project

class PositionpracticeAdmin(admin.ModelAdmin):
    model = Positionpractice

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Practice)
admin.site.register(Positionpractice, PositionpracticeAdmin)