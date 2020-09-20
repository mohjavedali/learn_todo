from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'todo_app'

    def __str__(self):
        return self.name
