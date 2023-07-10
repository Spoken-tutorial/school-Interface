from django.contrib import admin

from .models import User, Organisation, School, Payment, TrainingTeam, \
        CentralCoordinator, SchoolCoordinator, Teacher, Parent, Profile, \
        Location, Condition, MessageType, Message


class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "is_active",
                    "date_joined", "phone"]
    list_editable = ['is_active']
    search_fields = ["first_name", "last_name", "email"]
    # exclude = ["password","last_login"]


class LocationAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "dob", "gender"]
    search_fields = ["user__first_name", "user__last_name", "user__email"]


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ["name_of_association", "type", "location", "date_of_association",
                    "type", "updated", "is_active"]
    list_filter = ['type']
    list_editable = ['is_active']
    search_fields = ["name_of_association"]


class SchoolAdmin(admin.ModelAdmin):
    list_display = ["name_of_association", "type", "organisation", "location",
                    "date_of_association", "type", "updated", "is_active"]
    list_filter = ["type"]
    list_editable = ['is_active']
    search_fields = ["name_of_association", "organisation__name_of_association"]


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["school", "organisation", "date_of_payment", "amount", "utr", "receipt"]
    list_filter = ["school__location__state"]
    # list_editable = ['is_active']
    search_fields = ["school__name_of_association",
                     "organisation__name_of_association", "utr"]


class TrainingTeamAdmin(admin.ModelAdmin):
    list_display = ["username"]
    search_fields = ["first_name", "last_name", "email"]


class CentralCoordinatorAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "organisation"]
    list_filter = ["organisation__location__state"]
    search_fields = ["first_name", "last_name", "email",
                     "organisation__name_of_association"]


class SchoolCoordinatorAdmin(admin.ModelAdmin):
    list_display = ["email", "school"]
    list_filter = ["school__location__state"]
    search_fields = ["first_name", "last_name", "email",
                     "school__name_of_association"]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["email", "school", "unique_id"]
    list_filter = ["school__location__state"]
    search_fields = ["first_name", "last_name", "email",
                     "school__name_of_association", "unique_id"]


class ParentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]
    search_fields = ["first_name", "last_name", "email"]
    search_fields = ["first_name", "last_name", "email"]


admin.site.register(User, UserAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(TrainingTeam, TrainingTeamAdmin)
admin.site.register(CentralCoordinator, CentralCoordinatorAdmin)
admin.site.register(SchoolCoordinator, SchoolCoordinatorAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Message)
admin.site.register(MessageType)
admin.site.register(Condition)
