from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Listings

@receiver(post_save, sender=Listings)
def send_listing_created_emails(sender, instance, created, **kwargs):
    if created:
        subject = "New Listing is created"
        message = render_to_string('emails/listing_created_email.txt', {'listing': instance})
        html_message = render_to_string('emails/listing_created_email.html', {'listing': instance})
        recipients_list = [instance.user.email]  

        send_count = send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients_list, html_message=html_message)

        if send_count > 0:
            print("Emails sent successfully")
        else:
            print("Failed to send email.")


