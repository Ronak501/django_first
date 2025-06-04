from django.contrib import admin
from .models import RonakVarity, RonakReview, Store, RonakCertificate

# Register your models here.
class RonakReviewInline(admin.TabularInline):
      model = RonakReview
      extra = 2

class RonakVarityAdmin(admin.ModelAdmin):
      list_display = ('name', 'type', 'date_added') 
      inlines = [RonakReviewInline]

class StoreAdmin(admin.ModelAdmin):
      list_display = ('name', 'location')
      filter_horizontal = ('ronaks',)

class RonakCertificateAdmin(admin.ModelAdmin):
      list_display = ('ronak', 'issued_date', 'valid_until')

admin.site.register(RonakVarity, RonakVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(RonakCertificate, RonakCertificateAdmin) 