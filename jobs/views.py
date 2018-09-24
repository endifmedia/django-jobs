from django.shortcuts import render

from django.http import HttpResponse

from .models import Job

#def detail(request, job_id):


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    job_list = Job.objects.all()
    # return HttpResponse("You're looking at question %s." % job_id)
    return render(request, 'index.html', {'job_list': job_list})
