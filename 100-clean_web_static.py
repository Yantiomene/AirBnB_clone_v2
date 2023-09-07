#!/usr/bin/python3

from fabric.api import *


env.user = "ubuntu"
env.hosts = ['54.162.106.171', '54.90.38.102']


def do_clean(number=0):
    """Clean the directory which contains the tar localy
    and the deployd file on the server"""

    number = int(number)
    number = 2 if number == 0 else (number + 1)

    local("cd versions ; ls -t | tail -n +{} | xargs rm -rf".format(number))
    direc = "/data/web_static/releases"
    run("cd {} ; ls -t | tail -n +{} | xargs rm -rf".format(direc, number))
