from django.db import models

STATUS = (("COMPLETE", 'Complete'),
          ("INCOMPLETE", 'Incomplete'),)


class Task(models.Model):
    task_name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    task_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS,
                              default='INCOMPLETE')
    owner = models.ForeignKey('auth.User', related_name='tasks',
                              on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.task_name}"
