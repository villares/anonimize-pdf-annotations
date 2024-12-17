#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pip/pyinstaller build script for app.

Install as Python package:
    python3 setup.py install

Create EXE/APP:
    python3 setup.py build_binary
"""

import os
import sys
import setuptools
import distutils.cmd

OSX_INFO_PLIST = "configs/osx/Info.plist"

NAME = 'remove_name_from_annotations_gui'
MAIN = 'remove_name_from_annotations_gui.py'


class BuildBinaryCommand(distutils.cmd.Command):
    description = 'build binary release'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    # noinspection PyShadowingNames
    def run(self):
        if sys.platform == 'darwin':
            with open(OSX_INFO_PLIST, 'r') as file:
                filedata = file.read()
            with open(OSX_INFO_PLIST, 'w') as file:
                file.write(filedata)

            command_gui = f'pyinstaller --noconfirm --onefile --windowed --noupx --name "{NAME}" --clean "./{MAIN}"'

            os.system(command_gui)

            exit(0)
        elif sys.platform == 'darwin_future_test':
            APP = ['remove_name_from_annotations_gui.py']
            OPTIONS = {
                'argv_emulation': True
            }
            setuptools.setup(
                app = APP,
                options = {'py2app': OPTIONS},
                setup_requires = ['py2app'])
        elif sys.platform == 'win32':
            command_gui = f'pyinstaller --noconfirm --onefile --windowed --noupx  --name "{NAME}" --clean  "./{MAIN}"'

            os.system(command_gui)

            exit(0)
        elif sys.platform == 'linux':
            command_gui = f'pyinstaller --noconfirm --onefile --windowed --noupx --name "{NAME}" --clean  "./{MAIN}"'

            os.system(command_gui)


            exit(0)
        else:
            exit(0)

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    cmdclass={
        'build_binary': BuildBinaryCommand,
    },
    name=NAME,
    author=' Alexandre B A Villares',
    description='A naive Python tool to remove your name from PDF annotations ',
    long_description=readme,
    url='https://github.com/villares/anonymize-pdf-annotations',
    license=license,
    keywords=['pdf', 'annotations', 'highlight', 'pymupdf', 'author'],
    packages=['remove_name_from_annotations_gui'],
    install_requires=[
        'PyMuPDF',
        'FreeSimpleGUI',
    ],
    classifiers=[],
    zip_safe=False,
)