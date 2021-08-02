from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"User object: {self.title} {self.description} ({self.id})"


class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(Books, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"User object: {self.first_name} {self.last_name} {self.notes} ({self.id})"