from django.shortcuts import render
from .signals import new_subscriber

# Create your views here.
from .models import *

def get_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})

def get_job(request,id):
    job = Job.objects.get(id=id)
    return render(request,'job.html',{'jobs':job})

def subscribe(request, id):
    if request.method == "POST":
        job = Job.objects.get(pk=id)
        sub = Subscriber(email=request.POST['email'])
        sub.save()
        subscription = Subscription(user=sub, job=job)
        subscription.save()
        new_subscriber.send(sender=Subscription, job=job, subscriber=sub)
        payload = {
        'job': job,
        'email': request.POST['email']
        }
        return render(request, 'subscribed.html', {'payload': payload})





 