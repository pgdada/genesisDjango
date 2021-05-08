from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = {"Name" : "Promise Dada",
            "Track" : "Backend(Python)",
            "IDEtype" : "VS Code",
            "GitHub" : "@pgdada",
            "Message" : "Maximum Effort!",
            }
    return render(request, 'myprofile.html', data)
    # return HttpResponse(data.values)