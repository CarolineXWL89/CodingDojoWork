from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# author = models.ForeignKey(Author, related_name="books", on_delete=models.PROTECT)
	# authors = models.ManyToManyField(Author, related_name="books")

	def __repr__(self):
		return("<Book object: {}, {}, {}>".format(self.name, self.desc, self.authors))

	def __str__(self):
		return self.name

class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# book = models.ForeignKey(Book, related_name="authors", on_delete=models.PROTECT)
	books = models.ManyToManyField(Book, related_name="authors")
	notes = models.TextField()

	def __str__(self):
		return("{} {}".format(self.first_name, self.last_name))

	def __repr__(self):
		return("<Author object: {} {}, {}, {}, {}>".format(self.first_name, self.last_name, self.email, self.books, self.notes))

