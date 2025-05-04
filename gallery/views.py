from django.shortcuts import render, redirect
from .forms import RegisterForm, PhotoForm
from .models import Photo
from django.contrib import messages
from django.conf import settings
import boto3
from botocore.exceptions import ClientError

# Home page view
def home(request):
    return render(request, 'home.html')

# Gallery view with S3 signed URLs
def gallery(request):
    if not request.user.is_authenticated:
        messages.info(request, "To access the gallery you need to log in.")
        return redirect('login')
    
    photos = Photo.objects.filter(user=request.user)
    
    # Generate presigned URLs for S3 access
    s3_client = boto3.client('s3',
                            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                            region_name=settings.AWS_S3_REGION_NAME)
    
    for photo in photos:
        try:
            photo.signed_url = s3_client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                    'Key': photo.image.name
                },
                ExpiresIn=3600
            )
        except ClientError as e:
            messages.error(request, f"Error accessing photo: {e}")
            photo.signed_url = None
    
    return render(request, 'gallery.html', {'photos': photos})

# User registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})

# Photo upload view
def upload_photo(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, "Image uploaded successfully")
            return redirect('gallery')
    else:
        form = PhotoForm()

    return render(request, 'upload.html', {'form': form})

# Photo deletion view
def delete_photo(request, photo_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    try:
        photo = Photo.objects.get(id=photo_id, user=request.user)
        photo.delete()
        messages.success(request, "Photo successfully deleted")
    except Photo.DoesNotExist:
        messages.error(request, "Photo not found or no permission")
    
    return redirect('gallery')