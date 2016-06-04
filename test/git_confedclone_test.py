# -*- coding: utf-8 -*-
from __future__ import print_function

import unittest
import yaml
import os

import git_confedclone

class GitConfedcloneTest(unittest.TestCase):
    SAMPLE_YAML = os.path.join(os.path.dirname(__file__), "sample.yaml")

    def test_parser(self):
        repo_info_https = git_confedclone.parse_repository("https://github.com/Hi-king/opentoonz_not.git")
        repo_info_ssh = git_confedclone.parse_repository("git@github.com:Hi-king/opentoonz_not.git")
        self.assertEqual(repo_info_https.host, repo_info_ssh.host)
        self.assertEqual(repo_info_https.uname, repo_info_ssh.uname)
        self.assertEqual(repo_info_https.host, "github.com")
        self.assertEqual(repo_info_https.uname, "Hi-king")

    def test_parser_bitbucket(self):
        repo_info_https = git_confedclone.parse_repository("https://Hi_king@bitbucket.org/Hi-king/test.git")
        self.assertEqual(repo_info_https.host, "bitbucket.org")
        self.assertEqual(repo_info_https.uname, "Hi-king")

    def test_get_switched_conf(self):
        with open(self.SAMPLE_YAML) as f:
            conf_dict = yaml.load(f)

        my_repo_info_https = git_confedclone.parse_repository("https://github.com/Hi-king/opentoonz_not.git")
        my_switched_conf = git_confedclone.get_switched_conf(my_repo_info_https, conf_dict)

        foo_repo_info_https = git_confedclone.parse_repository("https://github.com/foo/opentoonz_not.git")
        foo_switched_conf = git_confedclone.get_switched_conf(foo_repo_info_https, conf_dict)

        self.assertTrue("user.email" in my_switched_conf)
        self.assertTrue("user.name" in my_switched_conf)
        self.assertTrue("user.email" in foo_switched_conf)
        self.assertTrue("user.name" in foo_switched_conf)
        self.assertNotEqual(my_switched_conf["user.name"], foo_switched_conf["user.name"])

if __name__ == '__main__':
    unittest.main()