# Create your views here.
from django.http import HttpResponse
from filesystem_explorer import hw as hw1

def hw(request):
    return HttpResponse(hw1())