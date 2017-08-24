from django.contrib import admin
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

def group(self, user):
    groups = []
    for group in user.groups.all():
        groups.append(group.name)
    return ' '.join(groups)
group.short_description = 'Groups'

UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'group')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)