from django.db import models
from django.dispatch import receiver
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

# Create your models here.

class Sucursal(models.Model):
    ciudad= models.CharField(max_length=50)
    sucursal= models.CharField(max_length=50)
    slug= models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.sucursal

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Sucursal)

@receiver(post_save, sender=Sucursal)
def ensure_sucursal_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Sucursal.objects.get_or_create(sucursal=kwargs.get('instance'))