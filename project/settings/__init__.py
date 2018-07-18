import os
DEBUG = os.environ['DEBUG']

if DEBUG == 'True':
    from .base import *
elif DEBUG == 'False':
    from .prodaction import *
