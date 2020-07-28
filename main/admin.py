from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(GameShots)
admin.site.register(Reviews)

