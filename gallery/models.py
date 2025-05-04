from django.db import models
from django.contrib.auth.models import User
from storages.backends.s3boto3 import S3Boto3Storage

# Custom upload path
def user_directory_path(instance, filename):
    return f'users/{instance.user.username}/{filename}'

# Photo model
class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=user_directory_path,
        storage=S3Boto3Storage()
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo {self.id} Of User {self.user.username}'