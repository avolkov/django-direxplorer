# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context, Template
from filesystem_explorer import listdir


def hw(request):
    #template = Template('templates/base.html')
    #template = Template("Hello, world!")
    #ctx = Context({'listing':listdir()})
    #return template.render(ctx)
    
    return render_to_response('base.html', {'data': listdir()}, context_instance=RequestContext(request))