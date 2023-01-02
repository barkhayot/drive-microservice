from django.contrib import admin

from .models import UserProfile, Account, Featured_Music, Featured_Pets, Featured_Smoking, Featured_Talking

admin.site.register(Account)
admin.site.register(UserProfile)
admin.site.register(Featured_Talking)
admin.site.register(Featured_Smoking)
admin.site.register(Featured_Pets)
admin.site.register(Featured_Music)