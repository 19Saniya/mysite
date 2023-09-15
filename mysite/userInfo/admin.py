from django.contrib import admin
from userInfo.models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('userInfo_name', 'userInfo_email', 'userInfo_phone', 'userInfo_comment')


admin.site.register(UserInfo, UserInfoAdmin)

# Register your models here.
