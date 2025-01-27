from django.contrib import admin
from jobscanner.models import *
from django.utils.html import format_html
from jobscanner.models import Attendee
from django.urls import reverse
from django.db.models import Field


class AttendeModel(admin.ModelAdmin):
    search_fields = (
        "email",
        "name",
        "phone_number"
    )

    list_filter = [
        "track",
        "location"
    ]

    list_display = ["name", "email", "track", "phone_number", "visits"]

    def profile_link(self, obj):
        # Generate a clickable link to the attendee's profile
        url = reverse("profile", kwargs={"pk": obj.pk})
        return format_html('<a href="{}" target="_blank">View Profile</a>', url)
    
    profile_link.short_description = 'Profile Link'

    def qr_code(self, obj):
        # Generate the QR code dynamically
        # Create a downloadable QR code link
        download_link = reverse("qr_code", kwargs={"pk": obj.pk})  # Custom admin URL for downloading
        return format_html(
            '<a href="{}" target="_blank">Download QR Code</a>', download_link
        )
    
    qr_code.short_description = 'QR Code'
    readonly_fields = ['profile_link', 'qr_code']


class RecrutierModel(admin.ModelAdmin):
    list_display = ('name', 'scanned_counts')

    def get_ordering(self, request):
        return ['-scanned_counts']
    

class ScanLogModel(admin.ModelAdmin):
    list_display = ('company', 'attendee', 'comment')
    
    def company(self, obj):
        return obj.recrutier.name

    def attendee(self, obj):
        return obj.attendee.name


# Register your models here.
admin.site.register(Attendee, AttendeModel)
admin.site.register(Recrutier, RecrutierModel)
admin.site.register(ScanLog, ScanLogModel)
