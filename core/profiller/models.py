from django.db import models

from django.contrib.auth.models import User
from PIL import Image

class Profil(models.Model):
    # Fast Access with 'Raleted Name' feature 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')

    bio = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to= 'profil_images/%Y/%m/')

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "Profiller"
    

    def save(self , *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.photo.path)


class ProfilState(models.Model):
    user_profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    state_message = models.CharField(max_length=240)
    created_time = models.DateTimeField(auto_now_add= True) # Yaratıldıkdan sonra Değişmeyen tarih
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_profil) # Instance geldiği için ve yazdırma işlemi olduğu için str eklendi
    
    class Meta:
        verbose_name_plural = "Profil Statement"