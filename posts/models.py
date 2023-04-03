from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='post_images/', blank=True, null=True)
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

# override the save method to generate the slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + '_' + str(self.id))
        return super().save(self, *args, **kwargs)
