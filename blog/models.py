from django.db import models
import random
import string


def generate_slug():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


class Toy(models.Model):
    groom = models.CharField(max_length=100)
    bride = models.CharField(max_length=100)
    wedding_date = models.DateTimeField()
    venue_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    card_number = models.CharField(max_length=50)
    card_owner = models.CharField(max_length=100)

    # MUSIQA UCHUN YANGI MAYDON
    # upload_to='wedding_music/' musiqalarni media/wedding_music papkasiga yuklaydi
    music = models.FileField(upload_to='wedding_music/', null=True, blank=True)

    slug = models.CharField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.groom} & {self.bride}"