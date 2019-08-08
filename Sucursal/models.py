from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Ubicacion(models.Model):
    ciudad=models.CharField(max_length=50)
    area=models.ManyToManyField("Areas")
    def __str__(self):
        return self.ciudad

class Areas(models.Model):
    area=models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50)
    slug= models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.area

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Areas)

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(usuario=kwargs.get('instance'))