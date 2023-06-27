from django.db import models
from account.models import UserData

class TodosData(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    todo_text = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    todo_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.todo_text