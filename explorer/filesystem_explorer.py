import os
from pprint import pprint as pp
from collections import OrderedDict

#def traverse_path(path):
#    os.walk(path)

mypath = '/home/alex/tmp'

def listdir(): 
    
    everything = os.listdir(mypath)  
    
    files = [k for k in everything if os.path.isfile(os.path.join(mypath, k)) ]
    directories = [k for k in everything if os.path.isdir(os.path.join(mypath, k)) ]
    
    files.sort()
    directories.sort()
    
    file_dict = OrderedDict([(x, ['file', os.path.getsize(os.path.join(mypath,x))]) for x in files])
    dir_dict = OrderedDict([(x, ['dir'])for x in directories])
    
    #import pdb; pdb.set_trace()   
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
