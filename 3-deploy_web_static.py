#!/usr/bin/python3
import os.path
from time import strftime
from datetime import date
from fabric.api import *

env.hosts = ['52.3.253.194', '34.207.154.42']


def do_pack():
    """ A Fabric script that generates a .tgz archive from the contents
        of the web_static
    """

    filename = strftime("%Y%m%d%H%M%S")
    file_ = "versions/web_static_{}.tgz".format(filename)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_)).failed is True:
        return None
    return file_


def do_deploy(archive_path):
    """ Deploy web files archive to server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file_ = archive_path.split("/")[-1]
    name = file_.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file_)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file_, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file_)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file_ = do_pack()
    if file_ is None:
        return False
    return do_deploy(file_)
