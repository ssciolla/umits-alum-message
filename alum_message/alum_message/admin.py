from django.contrib import admin

# Register your models here.
import alum_message.models as models

class ReceiptInline(admin.TabularInline):
    model = models.Message.recipients.through

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ['sender_alum', 'subject', 'message_text']
    list_display = ['timestamp', 'sender_alum', 'display_recipients', 'subject', 'message_text']
    inlines = [ReceiptInline]

@admin.register(models.Alum)
class AlumAdmin(admin.ModelAdmin):
    fields = ['uniqname', 'display_name', 'family_name', 'given_name']
    list_display = ['uniqname', 'display_name', 'family_name', 'given_name']