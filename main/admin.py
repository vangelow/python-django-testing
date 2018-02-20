# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Projects, Category



# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_category')
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title',)

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Category, CategoryAdmin)


