"""
Provides amended os functions
"""

import os
from shutil import rmtree


def make_dir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def remove_dir(directory):
    if os.path.exists(directory):
        rmtree(directory)
