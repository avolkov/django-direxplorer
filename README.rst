===============
django-direxplorer -- http directory explorer for Django
===============

Overview
=========
The purpose of this program is to enable multiple file/directory transfer over http without the use of ftp sftp or other file transfer protocols. 
The functionality implemented by either transferring raw file content, archived file content or recursively archived directories.

Limitations
===============
This application performs no caching, so the server could easily be DOSed meaning that file transfer is only allowed for registered users.
The program implemented by first zipping all content in a file in /tmp directory and then sending it to the user, so be sure to enable ample timeout options on your upstream server, and have enough space in /tmp.

Installation
===============

 1. Copy django-direxplorer in your existing django project
 2. In settings.py
 	a. Add variable EXPLORER_URL="<yourpath>" this would declare base url for django-direxplorer to handle
 	b. Add django-direxplorer to your INSTALLED_APPS tuple
 	c. Make sure that you have the following apps enabled:
 		* django.contrib.auth
 		* django.contrib.contenttypes
 		* django.contrib.admin
 3. In urs.py add the following lines
 	a. An import statements
		from django.conf import settings
 	b. A urlpattern
 		(r'^%s/' % settings.EXPLORER_URL, include('django-direxplorer.urls')),
 4. Run **python manage.py syncdb**
 5. Go to admin interface -> Explorer Sites and add explorer site
 	a. Web URL: url for each site i.e. http://django-site/<EXPLORER_URL>/<WEB_URL>
 	b. Filesystem Path: a path on filesystem that will be accessed through web interface
  