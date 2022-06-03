from django.contrib import admin
from .models import matchNo, matchDetails, Stream, PlayerDetails
# Register your models here.
admin.site.register(matchNo)
admin.site.register(matchDetails)
admin.site.register(Stream)
admin.site.register(PlayerDetails)