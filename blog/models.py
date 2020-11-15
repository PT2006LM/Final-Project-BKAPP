from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField



class BlogAppAbstractModel(models.Model):
    author = models.ForeignKey(User, 
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        abstract = True
        ordering = ['-created_at']



class Blog(BlogAppAbstractModel):
    title = models.CharField(max_length=50, unique=True)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title


class Comment(BlogAppAbstractModel):
    content = RichTextField()
    test = models.CharField(max_length=20, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Reply(BlogAppAbstractModel):
    content = RichTextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)