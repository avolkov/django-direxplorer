# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context, Template
from filesystem_explorer import listdir, root_path
import os.path


def hw(request):
    #template = Template('templates/base.html')
    #template = Template("Hello, world!")
    #ctx = Context({'listing':listdir()})
    #return template.render(ctx)
    return render_to_response('base.html', {'data': listdir(root_path)}, context_instance=RequestContext(request))

def zip(request):
    response = HttpResponse(mimetype='application/zip')
    response['content-Disposition'] = "attachment; filename=%s.zip" % request.path.split("/")[-2]
    response.write('0'*50)
    return response
    #import pdb; pdb.set_trace()
    #return HttpResponse("Returning zipped data")
    #return render_to_response("Returning zipped data")
def explore(request):
    url_path = "/".join(request.META['PATH_INFO'].split('/')[2:])
    fs_path = os.path.join(root_path, url_path)
    #import ipdb; ipdb.set_trace()
    #return HttpResponse("Exploring: %s" % file_path)
    return render_to_response('base.html', {'data': listdir(fs_path, url_path)}, context_instance=RequestContext(request))