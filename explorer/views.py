# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context, Template
from filesystem_explorer import listdir, root_path, fe_mime, arc_zip
import os.path




def hw(request):
    return render_to_response('base.html', {'data': listdir(root_path)}, context_instance=RequestContext(request))

def zip(request):
    response = HttpResponse(mimetype='application/zip')
    response['content-Disposition'] = "attachment; filename=%s.zip" % request.path.split("/")[-2]
    response.write('0'*50)
    return response
def raw(request):
    url_path = "/".join(request.META['PATH_INFO'].split('/')[2:-1])
    fullpath = os.path.join(root_path, url_path)
    response = HttpResponse(open(fullpath, 'r'),mimetype=fe_mime.guess_type(url_path)[0])
    response['content-Disposition'] = "attachment; filename=%s" % fullpath.split('/')[-1]
    response['Content-Length'] = os.path.getsize(fullpath)
    return response
def explore(request):
    url_path = "/".join(request.META['PATH_INFO'].split('/')[2:])
    return render_to_response('base.html', {'data': listdir(root_path, url_path)}, context_instance=RequestContext(request))