"""Bite 161. Count the number of files and directories
"""
import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    lst = [(len(dirs), len(files)) for _, dirs, files in os.walk(directory)]
    return tuple(sum(x) for x in zip(*lst))
