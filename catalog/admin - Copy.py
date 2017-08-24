from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

'''class SBUserAdmin(UserAdmin):
    list_filter = UserAdmin.list_filter + ('groups__name',)
    list_display = ('username','custom_group', )

    def custom_group(self, obj):
        """
        get group, separate by comma, and display empty string if user has no group
        """
        return ','.join([g.name for g in obj.groups.all()]) if obj.groups.count() else ''

admin.site.unregister(User)
admin.site.register(User, SBUserAdmin)'''

UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)