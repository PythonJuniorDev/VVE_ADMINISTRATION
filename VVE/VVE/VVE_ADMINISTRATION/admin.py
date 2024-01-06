from django.contrib import admin
from .models import Resident, BoardMember, Repair, MeetingDate, External_Partie


class ResidentAdmin(admin.ModelAdmin):
    '''Shows the fields below in the Admin'''
    list_display = ["first_name", "last_name", "address", "phone_number"]
    list_filter = ["first_name", "last_name", "address", "phone_number"]
    search_fields = ["first_name", "last_name", "address", "phone_number"]
    ordering = ["first_name"]
    list_per_page = 3
    prepopulated_fields = {"first_name": ["first_name"]}


class BoardMemberAdmin(admin.ModelAdmin):
    '''Shows the fields below in the Admin'''
    list_display = ["first_name", "last_name", "address", "phone_number"]
    list_filter = ["first_name", "last_name", "address", "phone_number"]
    search_fields = ["first_name", "last_name", "address", "phone_number"]
    ordering = ["first_name"]
    list_per_page = 3
    #prepopulated_fields = {"name": ["organisation"]}


class RepairAdmin(admin.ModelAdmin):
    '''Shows the fields below in the Admin'''
    list_display = ["type_of_repair", "costs_incl_VAT", "VAT_percentage"]
    list_filter = ["type_of_repair", "costs_incl_VAT", "VAT_percentage"]
    search_fields = ["type_of_repair", "costs_incl_VAT", "VAT_percentage"]
    ordering = ["type_of_repair"]
    list_per_page = 3
    #prepopulated_fields = {"name": ["organisation"]}


class MeetingDateAdmin(admin.ModelAdmin):
    '''Shows the fields below in the Admin'''
    list_display = ["date"]
    list_filter = ["date"]
    search_fields = ["date"]
    ordering = ["date"]
    list_per_page = 3
    #prepopulated_fields = {"name": ["organisation"]}


class External_PartieAdmin(admin.ModelAdmin):
    '''Shows the fields below in the Admin'''
    list_display = ["company_name", "type_of_company"]
    list_filter = ["company_name", "type_of_company"]
    search_fields = ["company_name", "address_company", "type_of_company"]
    ordering = ["company_name"]
    list_per_page = 3
    #prepopulated_fields = {"name": ["organisation"]}


admin.site.register(Resident, ResidentAdmin)
admin.site.register(BoardMember, BoardMemberAdmin)
admin.site.register(Repair, RepairAdmin)
admin.site.register(MeetingDate, MeetingDateAdmin)
admin.site.register(External_Partie, External_PartieAdmin)