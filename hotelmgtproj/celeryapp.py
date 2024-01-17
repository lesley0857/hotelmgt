
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotelmgtproj.settings')

app = Celery('hotelmgtproj')
# app.conf.enable_utc = False
# app.conf.update(timezone ='Africa/Nigeria')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    # 'Happy Birthday mails by 6am': {
    #     'task': 'userapp.tasks.Send_birthday_mail',
    #     'schedule': crontab(hour=11, minute=45),
    #     # 'args': ()
    # },
    # checks database everyday by 9:27am and deletes all accounts that have not been verified after 24hrs.
    # 'Delete 24hrs old unverified mail': {
    #     'task': 'userapp.tasks.Delete_unverified_mail',
    #     'schedule': crontab(hour=10, minute=27),  # 1 hour behind Nigerian time
    # }
}
# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)  # ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
