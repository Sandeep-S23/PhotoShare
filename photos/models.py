from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):

	class Meta:
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')
		ordering = ['id']

	name = models.CharField(max_length=100, null=False, blank=False)	

	def __str__(self):
		return self.name

class Photo(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	description = models.TextField()
	image = models.ImageField(null=False, blank=False)

	def __str__(self):
		return self.description			
