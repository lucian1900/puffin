#!/usr/bin/env python3

import os
import sys
import subprocess

from contextlib import contextmanager

from distutils.core import setup, Command


@contextmanager
def chdir(d):
    cwd= os.getcwd()
    os.chdir(d)
    try: yield
    finally: os.chdir(cwd)

class ParrotCommand(Command):
    description = 'proxy for a parrot distutils command'
    user_options = []

    path = 'objects'
    command = ''

    def initialize_options(self): pass
    def finalize_options(self): pass

    def run(self):
        with chdir(self.path):
            proc = subprocess.Popen(
                    ['winxed', '--nowarn', 'setup.winxed', self.command],
                    stdout=subprocess.PIPE)
        
        print(proc.communicate()[0].decode(sys.getdefaultencoding()))

class ParrotBuild(ParrotCommand):
    command = 'build'

class ParrotClean(ParrotCommand):
    command = 'clean'


setup(
    name = 'puffin',
    packages = ['puffin'],
    version = '0.0.0',
    description = 'Python3 on Parrot',
    author = 'Lucian Branescu Mihaila',
    author_email = 'lucian.branescu@gmail.com',
    url = 'http://bitbucket.org/lucian1900/puffin',

    cmdclass = {'buildp': ParrotBuild,
                'cleanp': ParrotClean,
                'testp': ParrotTest,
    },
)
