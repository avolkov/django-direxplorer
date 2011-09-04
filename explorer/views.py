# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context, Template


from filesystem_explorer import listdir, root_path, fe_mime, arc_sio_zip, get_site_map

import os.path


###Get all admin objects



###replace root_path variable with database values
## refactor two leading lines in functions zip and raw into a separate function
def get_site_url(request):
    site_name = request.META['PATH_INFO'].split('/')[2]
    if site_name not in get_site_map().keys():
        return None
    root_path = get_site_map()[site_name]
    url_path = "/".join(request.META['PATH_INFO'].split('/')[3:])
    #import ipdb; ipdb.set_trace()
    return (site_name, root_path, url_path)

def zip(request):
    site_info = get_site_url(request)
    if site_info is None:
        return HttpResponse("Error, invalid site url")
    site_name,root_path, url_path = site_info
    sio_zip = arc_sio_zip(root_path, url_path)
    response = HttpResponse(mimetype='application/zip')
    response['content-Disposition'] = "attachment; filename=%s.zip" % request.path.split("/")[-2]
    response.write(sio_zip.read())
    sio_zip.close()    
    return response
def raw(request):
    url_path = "/".join(request.META['PATH_INFO'].split('/')[2:-1])
    fullpath = os.path.join(root_path, url_path)
    response = HttpResponse(open(fullpath, 'r'),mimetype=fe_mime.guess_type(url_path)[0])
    response['content-Disposition'] = "attachment; filename=%s" % fullpath.split('/')[-1]
    response['Content-Length'] = os.path.getsize(fullpath)
    return response
def explore(request):
    site_info = get_site_url(request)
    if site_info is None:
        return HttpResponse("Error, invalid site url")
    site_name,root_path, url_path = site_info
    return render_to_response('base.html', {'data': listdir(root_path, url_path, site_name)}, context_instance=RequestContext(request))