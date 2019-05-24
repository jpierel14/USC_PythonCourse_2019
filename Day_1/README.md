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

#### Important Information

| Keys and Unix Definitions   | Description                                     |
| -----------                 | -----------                                     |
|<kbd>CTRL</kbd>+<kbd>C</kbd> | Kills the running program, use if the program is running too long, outputting too much text to the screen, or running into errors. |
|<kbd>TAB</kbd>               | Using the TAB key, especially when navigating the filesystem, can help. Just start typing the beginning of the folder, file or program that you want to use, then hit the TAB key, the computer will try to guess what you are doing and fill in the rest. If the computer doesn't know what you want hitting the TAB key multiple times often gives you more options to choose from. |
| `.`                         | Current directory                               |
| `..`                        | Directory one up in the structure               |
| `~`                         | $HOME directoy, on linux `/home/<username>`, on mac `/Users/<username>` |


#### Basic file system operations

| Command               |  Description                                          |
| -----------           | -----------                                           |
| `ls`                  | list files in a directory                             |
| `cd <folder_name>`    | change directory into folder_name                     |
| `cd ..`               | move up one folder in directory structure             |
| `cd` or `cd ~`        | change directory into the $HOME folder of the user    |
|`pwd`                  | Prints the working directory                          |
| `mkdir <directoy>`    |  Make a new directory                                 |
| `rm <file_name>`      | *** WARNING ***<br>Removes file. They will be gone forever.<br>They are not stored in a trash/recycle bin. |
| `rm -r <folder_name>` | *** WARNING ***<br>Removes folder. They will be gone forever.<br>They are not stored in a trash/recycle bin. |
| `echo <variable>`     | Prints the variable to the screen                     |
| `touch`               | "touches" A file either updating it's modification date or creating it if it's not there. |

#### Finding things
| Command               |  Description                                          |
| -----------           | -----------                                           |
|  `find`               | |
|  `grep`               | |
|  `history`            | |

#### Downloading Files
| Command               |  Description                                          |
| -----------           | -----------                                           |
| `scp <username>@<hostname_ipaddress>:</path/to/file/download.tar.gz>`       | |
| `wget <url_to_download>` | |
| `curl <url_to_download>` | |

#### Putting operations together
| Command               |  Description |  Example       |
| -----------           | -----------  | -----------    |
| `>`                   | | |
| `\|`                  | | |
| `<`                   | | |
| `&&`                  | | |
| `;`                   | | |

#### Monitoring your system
| Command               |  Description                                          |
| -----------           | -----------                                           |
| `top`                 | |
| `htop`                | |
| `df`                  | |
| `du`                  | |

#### Environment Variables

| Command                         |  Description                                |
| -----------                     | -----------                                 |
| `.bashrc` `.cshrc` `.login`     | |
| `export` `setenv`               | |
| `PATH`                          | |
| `PYTHONPATH`                    | |
| `LD_LIBRARY_PATH` `DYLD_LIBRARY_PATH` | -- talk about dynamic libraries `*.so/*.dyld` |


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
