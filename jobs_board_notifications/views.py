from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from jobs_board_main.signals import new_subscriber
from jobs_board_main.models import Job, Subscriber, Subscription

@receiver(new_subscriber, sender=Subscription)
def handle_new_subscription(sender, **kwargs):
    subscriber = kwargs['subscriber']
    job = kwargs['job']

    msg = """User {} has just subscribed to the Job {}.
    """.format(subscriber.email, job.title)

    print(msg)
    send_mail(f"New Subscription for {job.title}", message=msg, EMAIL_HOST_USER = "akshay@jobnotify.com", recipient_list=[job.company_mail], fail_silently = False)