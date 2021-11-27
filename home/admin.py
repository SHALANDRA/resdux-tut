from django.contrib import admin


from .models import crms

# Register your models here.
#@admin.register(crms)
class crmsAdmin(admin.ModelAdmin):
    list_display = ('profile_id','client_name','email', 'prop_id','description')
    #list_display=('profile_id',' description',)
    #list_filter = ('profile_id','description',)
#admin.site.unregister(crms)
admin.site.register(crms,crmsAdmin) 
