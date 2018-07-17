import os
if os.environ['DEBUG']:
    from .base import *
else:
    from .prodaction import *
