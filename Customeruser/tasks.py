from celery import shared_task
import os
from django.template.loader import render_to_string
from django.conf import settings
import json
from django.core.mail import EmailMessage
from .models import CustomBaseuser
from datetime import timedelta, date, time


@shared_task(bind=True)
def send_email_task(self, subject, from_email, serialized_token, to):
    token = json.loads(serialized_token)
    link = f'http://localhost:3000/verify/{token}'
    html_content = render_to_string(
        ['verify_email.html'], {'link': link})
    message = EmailMessage(subject=subject,
                           body=html_content,
                           from_email=from_email,
                           to=[to],)
    message.content_subtype = 'html'
    message.send()
    return 'Task Done'


# @shared_task(bind=True)
# def Send_reset_password_email(self, serialized_token, subject, from_email, to):
#     token = json.loads(serialized_token)
#     link = f'http://localhost:3000/Password_Reset/{token}'
#     html_content = render_to_string(
#         ['reset_password.html'], {'password_reset_link': link})
#     message = EmailMessage(subject=subject,
#                            body=html_content,
#                            from_email=from_email,
#                            to=[to],)
#     message.content_subtype = 'html'
#     message.send()
#     return 'Email Sent'


# @shared_task(bind=True)
# def Send_birthday_mail(self):
#     celebrants = Custombaseuser.objects.filter(birth_date=date.today())
#     for celebrant in celebrants:
#         html_content = render_to_string(
#             ['birthday_template.html'], {'celebrant': celebrant})
#         message = EmailMessage(subject=f'Happy Birthday {celebrant.firstname}',
#                                body=html_content,
#                                from_email='nwekelesley@gmail.com',
#                                to=[f'{celebrant.email}'],)
#         message.content_subtype = 'html'
#         message.send()
#     return 'Birthday Wish Sent'


# @shared_task(bind=True)
# def Delete_unverified_mail(self):
#     emails_deleted = []
#     unverified_users = Custombaseuser.objects.filter(email_verified=False)
#     for user in unverified_users:
#         if user.joined_date+timedelta(hours=24):
#             print(f'{user}')
#             societies = Usersocities.objects.filter(user=user.id)
#             [i.delete() for i in societies]
#             emails_deleted.append(user.email)
#             user.delete()
#     return f'The following emails: {emails_deleted} were deleted'
