#!/usr/bin/python3
'''
Script generates tgz archize from contect of web_static
'''

from os.path import isdir
from datetime import datetime
from fabric.api import local


def do_pack():
    ''' generates a tgz archive '''
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
