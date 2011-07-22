#!/usr/bin/env python3

import os
import subprocess
from glob import glob

from distutils.core import setup, Command

class ParrotCommand(Command):
    description = 'proxy for a parrot distutils command'
    user_options = []

    def initialize_options(self):
        self.command = ''

    def finalize_options(self): pass

    def run(self):
        setup_path = os.path.join('objects', 'setup.winxed')

        proc = subprocess.Popen(['winxed', setup_path, self.command],
                               stdout=subprocess.PIPE)
        
        print(proc.communicate()[0])

class ParrotBuild(ParrotCommand):
    description = 'command that builds all winxed files in objects/, generating .pbc'

    def initialize_options(self):
        self.command = 'build'

class ParrotClean(ParrotCommand):
    description = 'Remove all .pbc and .pir files from objects/'

    def initialize_options(self):
        self.command = 'clean'

setup(
    name = 'puffin',
    packages = ['puffin'],
    version = '0.0.0',
    description = 'Python3 on Parrot',
    author = 'Lucian Branescu Mihaila',
    author_email = 'lucian.branescu@gmail.com',
    url = 'http://bitbucket.org/lucian1900/puffin',

    cmdclass = {'pbuild': ParrotBuild,
                'pclean': ParrotClean,
    },
)
