#taken from https://github.com/pallets/flask/wiki/Large-app-how-to
import os
import readline
from pprint import pprint

from flask import *
from SuperDiffer import *

os.environ['PYTHONINSPECT'] = 'True'