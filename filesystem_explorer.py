import os
import zipfile
import mimetypes as fe_mime
from collections import OrderedDict
from functools import partial


from django.conf import settings

from models import ExplorerSite
fe_mime.init()



def listdir(root_path, rel_path='', site_name=''):
    """Display directories and walk through their content""" 
    mypath = os.path.join(root_path, rel_path)
    everything = os.listdir(mypath)  
    fullpaths = map(lambda x: os.path.join(mypath,x),  everything)
    
    files = []
    directories = []
    
    for item, fullpath in zip(everything, fullpaths):
        if os.path.isfile(fullpath): files.append(item)
        if os.path.isdir(fullpath): directories.append(item)
    
    files.sort()
    directories.sort()
    
    join_url = partial(os.path.join,"/", settings.EXPLORER_URL, site_name, rel_path)
    file_dict = OrderedDict([(x, [join_url(x), 'file', os.path.getsize(os.path.join(mypath,x))]) for x in files])
    dir_dict = OrderedDict([(x, [join_url(x), 'dir'])for x in directories])
    
    upper_level = ''
    if rel_path:
        upper_level = "/".join(rel_path.split("/")[:-1])
        upper_level = os.path.join("/", settings.EXPLORER_URL, site_name, upper_level)
        print upper_level
    return (upper_level, dir_dict, file_dict)

def arc_sio_zip(root_path, rel_path, tempfile):
    """Recursively archive files/directories using StringIO"""
    sio_obj = tempfile
    pwd = os.getcwd()
    dest_dir = rel_path.split("/")[-1]
    
    os.chdir(os.path.join(root_path, "/".join(rel_path.split("/")[:-1])))
    zip_obj = zipfile.ZipFile(sio_obj, 'w', zipfile.ZIP_DEFLATED)
    if os.path.isdir(dest_dir):
        for directory,_,files in (k for k in os.walk(dest_dir) if len(k[2])> 0):
            for f in files:
                zip_obj.write(os.path.join(directory, f))
    elif os.path.isfile(dest_dir):
        zip_obj.write(os.path.join(dest_dir))
    
    zip_obj.close()
    sio_obj.seek(0)
    os.chdir(pwd)
    return sio_obj
def get_site_map():
    """Get available sites registered in admin"""
    site_maps = {}
    for site in ExplorerSite.objects.all():
        site_maps[site.web_url] = site.fs_path
    return site_maps