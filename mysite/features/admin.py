from django.contrib import admin
from features.models import Features
class FeaturesAdmin(admin.ModelAdmin):
    list_display=('features_icon','features_title','features_des')

admin.site.register(Features,FeaturesAdmin)
# Register your models here.
