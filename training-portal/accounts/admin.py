from django.contrib import admin
from accounts.models import Account, ContentCreator, SkillLevel, Trainee

        
class BaseAccountModelAdmin(admin.ModelAdmin):
    list_display = ("full_name", "username", "email", "is_active")
    
    def full_name(self, obj):
        return f"{obj.account.first_name} {obj.account.last_name}"
    
    def email(self,obj):
        return obj.account.email

    def username(self,obj):
        return obj.account.username
    
    def is_active(self,obj):
        return obj.account.is_active

class AccountModelAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "full_name", "account_type", 'account_type', 'is_active')
    search_fields = ("first_name", "last_name", "email", "username")
    exclude = ['password']
    list_filter = ('is_active', 'account_type')
    
    def account_type(self, obj):
        return "Trainee"  if obj.account_type == 'trainee' else "Content Creator"
    
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


admin.site.register(Account, AccountModelAdmin)
admin.site.register(Trainee, BaseAccountModelAdmin)
admin.site.register(ContentCreator, BaseAccountModelAdmin)
admin.site.register(SkillLevel)
