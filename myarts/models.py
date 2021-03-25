from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

class Article(models.Model):
    title = models.CharField(
        max_length=250,
        help_text='Enter the title of your article',
        validators=[MinLengthValidator(
            1, "Title must have more than 1 character"
        )]
    )
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
