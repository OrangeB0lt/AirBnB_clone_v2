#!/usr/bin/python3
''' Script based on 2-do_deploy_web_static, creates amd dist am archive '''

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['35.196.166.174', '34.74.134.64']

def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fileName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fileName))
        return fileName
    except:
        return None

def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        fileNew = archive_path.split("/")[-1]
        noExt = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, noExt))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fileNew, path, noExt))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, noExt))
        run('rm -rf {}{}/web_static'.format(path, noExt))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, noExt))
        return True
    except:
        return False

def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
