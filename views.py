from django.shortcuts import render
import requests
from subprocess import run, PIPE
import sys

def external(requests):
    username = requests.POST.get("username")
    password = requests.POST.get("password")
    out = run(sys.executable, ['//Users//ishu//Documents//uOttaHack 4//login.py', 
    username, password], shell=False,stdout= PIPE)
    print(out)
    return render(requests, 'index.html'{'data1': out.stdout)