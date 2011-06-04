#!/usr/bin/env python3

import os
import subprocess
from glob import glob

from distutils.core import setup, Command

class build_winxed(Command):
    description = 'command that builds all winxed files in objects/, generating .pbc'
    user_options = []

    def initialize_options(self):
        self.target_dir = 'objects'

    def finalize_options(self): pass

    def find_files(self, ext):
        files = os.listdir(self.target_dir)

        return [i for i in files 
                if i.endswith(ext) and not i.startswith('test_')]

    def compile_winxed(self, src):
        #print('Building {0}'.format(src))
        
        src_path = os.path.join(self.target_dir, src)
        
        proc = subprocess.Popen(['winxed', '--nowarn', '-c', src_path],
                                stdout=subprocess.PIPE)

        output = proc.communicate()[0]

    def compile_pir(self, src):
        print('Building {0}'.format(src))

        src_path = os.path.join(self.target_dir, src)
        pbc_path = src_path.replace('.pir', '.pbc')

        proc = subprocess.Popen(['parrot', '-o', pbc_path, src_path],
                                stdout=subprocess.PIPE)

        output = proc.communicate()[0]

    def run(self):
        for i in self.find_files('.winxed'):
            self.compile_winxed(i)

        for i in self.find_files('.pir'):
            self.compile_pir(i)

class clean_winxed(Command):
    description = 'Remove all .pbc and .pir files from objects/'
    user_options = []

    def initialize_options(self):
        self.target_dir = 'objects'

    def finalize_options(self): pass

    def run(self):
        pir_paths = glob(os.path.join(self.target_dir, '*.pir'))
        pbc_paths = glob(os.path.join(self.target_dir, '*.pbc'))

        for i in pir_paths + pbc_paths:
            os.remove(i)

setup(
    name = 'puffin',
    packages = ['puffin'],
    version = '0.0.0',
    description = 'Python3 on Parrot',
    author = 'Lucian Branescu Mihaila',
    author_email = 'lucian.branescu@gmail.com',
    url = 'http://bitbucket.org/lucian1900/puffin',

    cmdclass = {'build_winxed': build_winxed,
                'clean_winxed': clean_winxed,
    },
)
