from os import system, name
from urllib.request import urlopen
import subprocess

def install(name):
    subprocess.call(['pip3', 'install', name])

def connection():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return "Active"
    except:
        return "InActive"

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def spaces(spaces):
    t = ""
    for space in range(spaces):
        t += " "
    return t

def tabs(tabs):
    t = ""
    for tab in range(tabs):
        t += "\t"
    return t

def ListtoStr(s, *args):
    new = ""
    for x in s:
        new += x
    return new
