from django.urls import path
from .views import gallery, upload_photo, delete_photo

urlpatterns = [
    path('', gallery, name='gallery'),
    path('upload/', upload_photo, name='upload'),
    path('delete/<int:photo_id>/', delete_photo, name='delete_photo'),
]