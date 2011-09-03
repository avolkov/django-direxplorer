import os
import zipfile
from pprint import pprint as pp
from collections import OrderedDict


#def traverse_path(path):
#    os.walk(path)

root_path = '/home/alex/tmp'

##refactor with basepath / relative_path
def listdir(mypath, relative_bit=''): 
    
    everything = os.listdir(mypath)  
    fullpaths = map(lambda x: os.path.join(mypath,x),  everything)
    
    files = []
    directories = []
    
    for item, fullpath in zip(everything, fullpaths):
        if os.path.isfile(fullpath): files.append(item)
        if os.path.isdir(fullpath): directories.append(item)
    
    files.sort()
    directories.sort()
    
    file_dict = OrderedDict([(x, ['file', os.path.getsize(os.path.join(mypath,x))]) for x in files])
    dir_dict = OrderedDict([(x, ['dir'])for x in directories])
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
