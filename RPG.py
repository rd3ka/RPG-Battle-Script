#!/usr/bin/env python3
import subprocess
from os import name

if name == 'nt':
    subprocess.call(['mode', 'con:cols=80', 'lines=100', './main.py'])
else:
    subprocess.call(['gnome-terminal', '--geometry=98x29', '--command=python3 main.py'])
