import os

from jsonfield.fields import JSONField

__version__ = open(os.path.join(os.path.dirname(__file__), 'VERSION')).read().strip()
