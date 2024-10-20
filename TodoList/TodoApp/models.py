from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name  # Display group name in admin panel or other interfaces

class Task(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='tasks')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
