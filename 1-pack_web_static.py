#!/usr/bin/python3
"""do_pack"""
import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """do_pack"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")

        archive = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive))
        return archive
    except:
        return None
