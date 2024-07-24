from django.contrib.auth.models import User
from profiller.models import Profil, ProfilState
from django.db.models.signals import post_save
from django.dispatch import receiver

# Eğer ben user üzerinden bir nesne yaratırsam, hemen save noktasından sonra burayı tetikle (trigger)
@receiver(post_save, sender=User) # Receiver = Alıcı Sender = Takip edilen 
def create_profil(sender, instance, created, **kwargs):
    # print(instance.username, '__Created: ', created)
    if created:
        Profil.objects.create(user = instance)


@receiver(post_save, sender=Profil) 
def create_first_state_message(sender, instance, created, **kwargs):
    if created:
        ProfilState.objects.create(
            user_profil = instance,
            state_message = f'{instance.user.username} R2Y ailesine katıldı.'
        )