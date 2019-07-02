# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse

class Alum(models.Model):
    alum_id = models.AutoField(primary_key=True)
    uniqname = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'alum'
        verbose_name = 'Alum'
        verbose_name_plural = 'Alumni'

    def __str__(self):
        return self.uniqname

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=300)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sender_alum = models.ForeignKey('Alum', models.CASCADE, related_name='sender')

    recipients = models.ManyToManyField('Alum', through='Receipt', related_name='recipients')

    class Meta:
        managed = False
        db_table = 'message'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    @property
    def display_recipients(self):
        """Create a string for alum_recipients. This is required to display in the Admin view."""
        receipts = self.receipts.select_related('alum', 'message')
        recipient_strings = []
        for receipt in receipts:
            recipient_string = receipt.alum.uniqname
            recipient_strings.append(recipient_string)
        return ', '.join(recipient_strings)

    def get_absolute_url(self):
        return reverse('message_detail', kwargs={'pk': self.pk})


class Receipt(models.Model):
    receipt_id = models.AutoField(primary_key=True)
    message = models.ForeignKey('Message', models.CASCADE, related_name='receipts')
    alum = models.ForeignKey('Alum', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'receipt'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
