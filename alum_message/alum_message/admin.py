from django.contrib import admin

# Register your models here.
import alum_message.models as models

class ReceiptInline(admin.TabularInline):
    model = models.Message.recipients.through

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ['alum_sender', 'thread', 'message_text']
    list_display = ['timestamp', 'alum_sender', 'thread', 'message_text', 'display_recipients']
    inlines = [ReceiptInline]

@admin.register(models.Alum)
class AlumAdmin(admin.ModelAdmin):
    fields = ['uniqname', 'password', 'display_name', 'family_name', 'given_name']
    list_display = ['uniqname', 'password', 'display_name', 'family_name', 'given_name']

@admin.register(models.Thread)
class ThreadAdmin(admin.ModelAdmin):
    fields = ['subject']
    list_display = ['subject']