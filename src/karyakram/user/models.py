from django.contrib.auth.models import AbstractUser

# We will create a custom user class,
# and point django settings to this.
# This will help us in adding any
# custom attributes in the future.
class User(AbstractUser):
    pass
