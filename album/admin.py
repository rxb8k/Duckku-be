from django.contrib import admin
from .models import Album, AlbumFrime, Photocard, PhotocardFrime, Artist, Music

admin.site.register(Album)
admin.site.register(AlbumFrime)
admin.site.register(Photocard)
admin.site.register(PhotocardFrime)
admin.site.register(Artist)
admin.site.register(Music)

# Register your models here.
