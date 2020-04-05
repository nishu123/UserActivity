from django.contrib import admin
from userapp.models import Members,Activity_Periods

# Register your models here.
# class MembersAdmin(admin.ModelAdmin):
#     list_display=['id','real_name','tz']
admin.site.register(Members)
admin.site.register(Activity_Periods)
