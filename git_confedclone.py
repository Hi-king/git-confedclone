#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import subprocess
import sys
import re
import os
try:
    from StringIO import StringIO
except:
    from io import StringIO
import yaml

def parse_repository(repository):
    class RepositoryPath(object):
        def __init__(self, clonestr):
            self.host = None
            self.uname = None

            if clonestr.find("://") >= 0: #http
                _protocol, path = clonestr.split("://")
                user_host, self.uname = path.split("/")[:2]
                self.host = user_host.split("@")[-1]
            else: #ssh
                _ssh_uname, host_path = clonestr.split("@")
                self.host, path = host_path.split(":")
                self.uname = path.split("/")[0]
    return RepositoryPath(repository)

def get_switched_conf(repository_info, conf_dict):
    if conf_dict is None: #conffile not found
        return {}
    for hostmatcher_string, hostmatched_value in [list(each_dict.items())[0] for each_dict in conf_dict]:
        if re.match(hostmatcher_string, repository_info.host):
            for usermatcher_string, conf in [list(each_hostmatched_dict.items())[0] for each_hostmatched_dict in  hostmatched_value]:
                if re.match(usermatcher_string, repository_info.uname):
                    return conf
    return {}

def find_conffile():
    if os.path.exists(os.path.expanduser("~/.gitconfedclone")):
        return open(os.path.expanduser("~/.gitconfedclone"))
    else:
        return StringIO() #works as void file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repository")
    args = parser.parse_args()

    parsed = parse_repository(args.repository)
    conf_dict = yaml.load(find_conffile())
    switched_conf = get_switched_conf(parsed, conf_dict)

    confstr = ""
    for key, value in switched_conf.items():
        print("{}: {}".format(key, value))
        confstr += " -c {}='{}' ".format(key, value)
    subprocess.call("git clone {confstr} {original}".format(confstr=confstr, original=" ".join(sys.argv[1:])), shell=True)

if __name__ == '__main__':
    main()
