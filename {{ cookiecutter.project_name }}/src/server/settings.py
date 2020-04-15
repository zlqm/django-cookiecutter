from .django_settings import *
from .extension_settings import *

try:
    # try to load develop settings
    # donnot add develop_settings into version control system!!!
    from .development_settings import *
except ImportError:
    pass
