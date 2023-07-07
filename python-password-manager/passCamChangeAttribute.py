from os import system
from os.path import dirname, abspath
from os.path import join as path_join
import sys
import win32api
import win32con


def change_file_attribute(filename):
    directory_path = dirname(abspath(__file__))
    file_path = path_join(directory_path, filename)
    if sys.platform.startswith("win"):
        if not win32api.GetFileAttributes(file_path) & win32con.FILE_ATTRIBUTE_SYSTEM:
            system("attrib +s +i +h {}".format(file_path))
