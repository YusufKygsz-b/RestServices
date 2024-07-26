from django.db import models
from django.conf import settings  # Özel kullanıcı modelini kullanmak için
from PIL import Image
from django.db.models import UniqueConstraint

class Profil(models.Model):
    # Fast Access with 'Raleted Name' feature 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profil')

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
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
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



## New Feaute has been added 25-07-2024

class Post(models.Model):
    user_info = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='post_images/%Y/%m/')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Post by {self.user_info}'
    
    class Meta:
        verbose_name_plural = "Posts"

    def save(self , *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.photo.path)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user_info = models.ForeignKey(Profil, on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user_info}'
    
    class Meta:
        verbose_name_plural = "Comments"



class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user_info = models.ForeignKey(Profil, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like by {self.user_info}'
    
    class Meta:
        unique_together = ('post', 'user')
        verbose_name_plural = "Likes"



class FriendRequest(models.Model):
    from_user = models.ForeignKey(Profil, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profil, related_name='received_requests', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Friend request from {self.from_user} to {self.to_user.username}'
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=['from_user', 'to_user'], name='unique_friend_request')
        ]
        verbose_name_plural = "Friend Requests"