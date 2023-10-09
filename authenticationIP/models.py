from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DecodeXCred(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # My Custom Modles

    DecodeXID = models.CharField(max_length=20, unique = True)

    class Meta:
        verbose_name = "UserCredentials"
        verbose_name_plural = "AdditionalUserCredentials"

    def __str__(self):
        return self.user.username