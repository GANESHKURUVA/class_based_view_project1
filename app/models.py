from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.topic_name