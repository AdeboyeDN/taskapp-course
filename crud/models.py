from django.db import models

class task(models.Model):
  task_name = models.CharField(max_length=500)
  is_completed = models.BooleanField(default=False)

  def __str__(self):
    return self.name