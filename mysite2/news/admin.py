from django.contrib import admin
from . models import berita,kategori,customuser
# Register your models here.

admin.site.register(customuser)

class kategoriAdmin(admin.ModelAdmin):
    list_display=['namakategori']
    search_fields=['namakategori']

admin.site.register(kategori,kategoriAdmin)

class beritaAdmin(admin.ModelAdmin):
    #list display
    list_display = ['judul','isi','kategori','gambar','penulis']
    search_fields = ['judul','kategori_name']
    autocomplete_fields = ['kategori']

admin.site.register(berita,beritaAdmin)
