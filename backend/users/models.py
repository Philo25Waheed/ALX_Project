from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        INSTRUCTOR = "INSTRUCTOR", "Instructor"
        STUDENT = "STUDENT", "Student"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.STUDENT)
    
    # Resolve conflicts with 'auth.User'
    # These are needed because we are inheriting from AbstractUser but replacing the default User model
    # Note: AbstractUser normally handles this, but explicit overrides can sometimes be safer if we had conflicts
    # However, since we set AUTH_USER_MODEL, we don't strictly need these related_name overrides unless we use 'auth.User' elsewhere
    # But to be safe and clean:
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    headline = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
