# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context, Template
from django.contrib.auth.decorators import login_required
from django.core.files.temp import NamedTemporaryFile


from filesystem_explorer import listdir, fe_mime, arc_sio_zip, get_site_map

import os.path


def get_site_url(request):
    """Parse url information"""
    site_name = request.META['PATH_INFO'].split('/')[2]
    if site_name not in get_site_map().keys():
        return None
    root_path = get_site_map()[site_name]
    url_path = request.META['PATH_INFO'].split('/')[3:]
    return (site_name, root_path, url_path)

@login_required
def zip(request):
    """Zip up files/directories"""
    site_info = get_site_url(request)
    if site_info is None:
        return HttpResponse("Error, invalid site url")
    site_name,root_path, url_path = site_info
    url_path = "/".join(url_path[:-1])
    sio_zip = arc_sio_zip(root_path, url_path, NamedTemporaryFile(mode='w'))
    response = HttpResponse(open(sio_zip.name, 'r'), mimetype='application/zip')
    response['content-Disposition'] = "attachment; filename=%s.zip" % request.path.split("/")[-2]
    response['Content-Length'] = os.path.getsize(sio_zip.name)
    return response

@login_required
def raw(request):
    """Serve raw files"""
    site_info = get_site_url(request)
    if site_info is None:
        return HttpResponse("Error, invalid site url")
    site_name,root_path, url_path = site_info
    url_path = "/".join(url_path[:-1])
    fullpath = os.path.join(root_path, url_path)
    response = HttpResponse(open(fullpath, 'r'),mimetype=fe_mime.guess_type(url_path)[0])
    response['content-Disposition'] = "attachment; filename=%s" % fullpath.split('/')[-1]
    response['Content-Length'] = os.path.getsize(fullpath)
    return response

@login_required
def explore(request):
    """Display directory contents"""
    site_info = get_site_url(request)
    if site_info is None:
        return HttpResponse("Error, invalid site url")
    site_name,root_path, url_path = site_info
    return render_to_response('base.html', {'data': listdir(root_path, "/".join(url_path), site_name)}, context_instance=RequestContext(request))