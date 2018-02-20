# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from django.db.models import permalink



def get_image_path():
	return false
# TODO : upload images with project ids on first upload **********
class Category (models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	description =  models.TextField(max_length=500, db_index=True)

	def __str__(self):
		return self.title

class Projects (models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	description = models.TextField(max_length=500,)
	image = models.ImageField(upload_to="projects/%Y/%m/%d")
	category = models.ForeignKey(Category, null=True)
	posted = models.DateField(db_index=True, auto_now_add=True)

	def __str__(self):
		return self.title

	def image_img(self):
   		if self.image:
	    		return u'%s' % self.image.url
		else:
			return 'No image found'
	def get_category(self):
		return self.category.title
		
	get_category.short_description = 'Category'
	image_img.short_description = 'Thumb'
	image_img.allow_tags = True

