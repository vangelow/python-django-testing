# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Projects
# Create your views here.

def index(request):
	projects = Projects.objects.all()[:10]
	context = {
		'projects': projects,
	}
	return render(request, 'main/index.html', context)