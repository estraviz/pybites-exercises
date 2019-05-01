"""Bite 161. Count the number of files and directories
"""
import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    number_of_directories = 0
    number_of_files = 0
    for _, dirs, files in os.walk(directory):
        number_of_directories += len(dirs)
        number_of_files += len(files)
    return (number_of_directories, number_of_files)
