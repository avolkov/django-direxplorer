import os
import zipfile
import mimetypes as fe_mime
from collections import OrderedDict
from StringIO import StringIO

from django.conf import settings

from models import ExplorerSite
#def traverse_path(path):
#    os.walk(path)

fe_mime.init()

##refactor with basepath / relative_path
def listdir(root_path, rel_path='', site_name=''): 
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
    file_dict = OrderedDict([(x, [os.path.join("/%s/%s" % (settings.EXPLORER_URL, site_name), rel_path, x), 'file', os.path.getsize(os.path.join(mypath,x))]) for x in files])
    dir_dict = OrderedDict([(x, [os.path.join("/%s/%s" % (settings.EXPLORER_URL, site_name), rel_path, x), 'dir'])for x in directories])
    ###use functools here to modify the paths
    
    #import ipdb; ipdb.set_trace()   
    return (dir_dict, file_dict)

def directory_walker(directory):
    '''
    for k in os.listdir(mypath):
        fullpath = os.path.join(mypath, k)
        if os.path.isfile(fullpath):
            entry[k] = [ 'file' ]
            entry[k].append(os.path.getsize(fullpath))
        elif os.path.isdir(fullpath):
            entry[k] = [ 'dir' ]
    #import pdb; pdb.set_trace()
    '''
    #for k in os.walk(mypath):
    #    print k
    #    import pdb; pdb.set_trace()

def arc_zip(path, filename):
    '''Archive every non-empty directory'''
    zip_obj = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
    for directory,_,files in (k for k in os.walk(path) if len(k[2])> 0):
        for f in files:
            zip_obj.write(os.path.join(directory, f))
    zip_obj.close()

def arc_sio_zip(root_path, rel_path):
    sio_obj = StringIO()
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
    site_maps = {}
    for site in ExplorerSite.objects.all():
        site_maps[site.web_url] = site.fs_path
    return site_maps