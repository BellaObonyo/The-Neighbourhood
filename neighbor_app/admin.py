from django.contrib import admin
from .models import Business, NeighborHood, Post, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(NeighborHood)