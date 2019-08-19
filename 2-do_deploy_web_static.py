#!/usr/bin/python3
'''
script based on file 1-pack_web that dist an archine to the WS
'''

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['35.196.166.174', '34.74.134.64']


def do_deploy(archive_path):
    ''' distributes an archive to WS '''
    if exists(archive_path) is False:
        return False
    try:
        fileNew = archive_path.split("/")[-1]
        noExt = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, noExt))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fileNew, path, noExt))
        run('rm /tmp/{}'.format(fileNew))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, noExt))
        run('rm -rf {}{}/web_static'.format(path, noExt))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, noExt))
        return True
    except:
        return False
