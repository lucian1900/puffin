#!/usr/bin/env python3

import os
import subprocess

from distutils.core import setup, Command

class build_winxed(Command):
    description = 'command that builds all winxed files in objects/, generating .pbc'
    user_options = []

    def initialize_options(self):
        self.cwd = None
        self.target_dir = 'objects'

    def finalize_options(self):
        self.cwd = os.getcwd()

    def find_files(self, ext):
        files = os.listdir(os.path.join(self.cwd, self.target_dir))

        return [i for i in files if i.endswith(ext)]

    def compile_winxed(self, src):
        print('Building file {0}'.format(src))
        
        src_path = os.path.join(self.cwd, self.target_dir, src)
        
        proc = subprocess.Popen(['winxed', '-c', src_path],
                                stdout=subprocess.PIPE)

        output = proc.communicate()[0]

    def compile_pir(self, src):
        print('Building file {0}'.format(src))

        src_path = os.path.join(self.cwd, self.target_dir, src)
        pbc_path = src_path.replace('.pir', '.pbc')

        print('src_path: {0}; pbc_path: {1}'.format(src_path, pbc_path))

        proc = subprocess.Popen(['parrot', '-o', pbc_path, src_path],
                                stdout=subprocess.PIPE)

        output = proc.communicate()[0]

    def run(self):
        for i in self.find_files('.winxed'):
            self.compile_winxed(i)

        for i in self.find_files('.pir'):
            self.compile_pir(i)

setup(
    name = 'puffin',
    packages = ['puffin'],
    version = '0.0.0',
    description = 'Python3 on Parrot',
    author = 'Lucian Branescu Mihaila',
    author_email = 'lucian.branescu@gmail.com',
    url = 'http://bitbucket.org/lucian1900/puffin',

    cmdclass = {'build_winxed': build_winxed,
    },
)
