
#This line has nothing to do with celery this line is here to make sure that 
# the celery imports does not clash with python
 
from __future__ import absolute_import, unicode_literals 
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')