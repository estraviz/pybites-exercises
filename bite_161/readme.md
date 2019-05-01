# Bite 161. Count the number of files and directories

Complete `count_dirs_and_files` traversing the passed in directory path.

Return a tuple of (*number_of_directories*, *number_of_files*)

Let's use the `tree` command to show an example:

```bash
$ mkdir -p project/a/1/I project/a/1/II project/a/2 project/b/1/I
tree project/
project/
├── a
│   ├── 1
│   │   ├── I
│   │   └── II
│   └── 2
└── b
    └── 1
        └── I

8 directories, 0 files
```

Your solution should match these counts:

```bash
$ python
>>> from tree import count_dirs_and_files
>>> count_dirs_and_files('project')
(8, 0)
```

Let's add two files:

```bash
$ touch project/a/1/I/bob
$ touch project/a/2/julian
$ python
>>> from tree import count_dirs_and_files
>>> count_dirs_and_files('project')
(8, 2)
```

Good luck and have fun!