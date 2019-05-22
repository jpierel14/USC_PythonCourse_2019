# Day 1 (The Basics)

## Installation/Python intro

## Programming Basic Terms:

- Variable
- List
- Dictionary
- Class
- Comprehension
- ...


## Unix Commands

These tutorials are based on using `bash/zsh/sh` as the shell. Most will work with different shells like `csh/tcsh` but your millage may vary. You can check the shell you are using by opening a terminal and running `echo $0`.

#### Important keys

Before starting to use the command line there are a few important keys to help you on your journey.

- <kbd>CTRL</kbd>+<kbd>C</kbd>

This is the ultimate end key. If your program is running too long, outputting too much to the screen, or running into errors, you can use ctrl-C to stop it.

- <kbd>TAB</kbd>

Typing is hard. Let the computer do it for you. Using the TAB key, especially when navigating the filesystem, can help. Just start typing the beginning of the folder, file or program that you want to use, then hit the TAB key, the computer will try to guess what you are doing and fill in the rest. If the computer doesn't know what you want hitting the TAB key multiple times often gives you more options to choose from.


#### Basic file system operations
- `ls` -- Lists the files in a directory
- `cd/./../~` -- Change the directory

. means current directory
.. means one directory up
~ is $HOME. Shortcut to get back home is `cd` without options.

- `pwd` -- Prints the working directory
- `mkdir` -- Make a new directory
- `rm` -- Remove files or folders
*** WARNINGS ***
`-rf` -- remove and force
This PERMANENTLY delete files. They will be gone forever. They are not stored in a trash/recycle bin.

- `echo` -- Print to the screen

Helpful in scripts or to check environment variables.

- `touch` -- "touches" A file either updating it's modification date or creating it if it's not there

#### Finding things
- `find`
- `grep`
- `history`

#### Downloading Files
- `scp`
- `wget/curl`

#### Putting operations together
- `> | <`
- `&&/;`

#### Monitoring your system
- `top/htop`
- `df/du`

#### Environment Variables
- `.bashrc/.login`
- `export/setenv`
- `PATH` -- order matters
- `PYTHONPATH`
- `LD_LIBRARY_PATH/DYLD_LIBRARY_PATH` -- talk about dynamic libraries `*.so/*.dyld`


## Git/Github
- git
- status
- add
- diff
- clone
- commit
- pull
- push
- fork
- ORIGIN/HEAD

Assignment:
  - cd into a folder
  - Create new file with your github username (touch/echo/>)
  - Add something to a python file to print
