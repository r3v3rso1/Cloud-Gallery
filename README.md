# Django Photo Storage with AWS S3

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![AWS](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

A Django application that allows users to upload, store, and manage their photos in private galleries using AWS S3 for storage, IAM for access management, and EC2 for deployment.
<br>
**Live Demo:** [https://cloudgallery.xyz](https://cloudgallery.xyz)

## Features

- User registration and authentication system
- Private photo galleries for each user
- Secure file uploads to AWS S3 bucket
- Presigned URLs for temporary access to private S3 objects
- Image validation (file type and size)
- Responsive design for all device sizes

## Technologies Used

- **Backend**: Django 4.x
- **Storage**: AWS S3
- **Authentication**: Django built-in + IAM
- **Deployment**: AWS EC2
- **Dependencies**: 
  - boto3
  - django-storages

## Installation

### Prerequisites

- Python 3.8+
- Django 4.x
- AWS account with S3, IAM configured
- EC2 instance (for deployment)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/r3v3rso1/Cloud-Gallery
   cd Cloud-Gallery

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate

3. Install dependencies:
   ```bash
    pip install -r requirements.txt

4. Configure environment variables:
   <br>
   Create a .env file or export them directly:
   ```bash
   AWS_ACCESS_KEY_ID=-your-key-
   AWS_SECRET_ACCESS_KEY=--your-key-
   SECRET_KEY=-your-django-insecure-

5. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser

6. Run the development server:
   ```bash
   python manage.py runserver

## ☁️ Deployment

You can deploy this app on AWS EC2 using:

    Gunicorn

    Nginx

    PostgreSQL or SQLite

    IAM user with S3 access permissions

Uploaded images are stored in S3 with path format:
<pre>users/&lt;username&gt;/&lt;filename&gt;</pre>
