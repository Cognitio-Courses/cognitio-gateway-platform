from django.contrib import admin

from trainings.models import Badge, Content, ContentTrainee, Technology, ThematicArea


class ContentModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'date']    
    
    def get_exclude(self, request, obj):
        user = request.user
        if not user.is_superuser:
            return ['creator']
    
    def get_queryset(self, request):
        queryset =  super().get_queryset(request)
        user = request.user
        if user.is_superuser:
            return queryset
        content_creator = user.content_creator
        return  queryset.filter(creator=content_creator)
    
    def save_model(self, request, obj, form, change):
        user = request.user
        if not user.is_superuser:
            content_creator = user.content_creator
            obj.creator = content_creator
        return super().save_model(request, obj, form, change)
    

class ContentTraineeModelAdmin(admin.ModelAdmin):
    list_display = ['trainee','trainee_full_name', 'content', 'badge', 'rate']
    list_filter = ('content',)
    search_fields = ('content__title',)
    readonly_fields = ('trainee', 'content', 'rate')
    
    
    def trainee_full_name(self, obj):
        return obj.trainee.account.get_full_name()
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user
        if user.is_superuser:
            return queryset
        return queryset.filter(content__creator=user.content_creator)
    
    


admin.site.register(ThematicArea)
admin.site.register(Technology)
admin.site.register(Badge)
admin.site.register(Content, ContentModelAdmin)
admin.site.register(ContentTrainee, ContentTraineeModelAdmin)

