import os
DEBUG = os.environ['DEBUG']

if DEBUG == 'True':
    from .base import *
else:
    from .prodaction import *
