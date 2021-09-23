import uuid
from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.
from django.utils.text import slugify


class Blog(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    desc = RichTextField()
    category = models.CharField(max_length=200)
    thumbnail_image = models.ImageField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.pk:
            name = self.name
            name.replace(" ", "-")
            self.slug = slugify(name + "-" + str(uuid.uuid1()))
        super(Blog, self).save(*args, **kwargs)


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)