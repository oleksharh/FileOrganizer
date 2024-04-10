This is a Python written script

## FileOrganizer

Sorts files into different folders which are previously declared in the variables section above the code.

Does it automatically in the background if you set it as task executable on windows

## Getting Started

- Firstly, check if you have all of the modules installed, if not here are needed modules:

```bash
pip install watchdog
# installs needed module watchdog

pip install pyinstaller
# installs pyinstaller needed for creating executable
```
- Secondly, look through the code and change your src_dir and dest_dir,

as well as destination folders and their extensions for your needs


- Lastly, run the code and check for any errors, if those appear and you know how to fix them let me know,

by creating a pull request, your help is appreciated

## Key Features

- Automatically moves(sorts) files into a different directory
- Works with a lot of file extensions
- Well suited for running on the background
- Will ease sorting downloaded files


## Don't Forget

Create an executable by running this code in terminal with organizer.py file open:

```bash
pyinstaller --onefile --noconsole organizer.py
```
It will create the executable that can be used with Task Scheduler on Windows

[Link to YouTube Tutorial "How to Create Automated Tasks on Windows 11"](https://www.youtube.com/watch?v=XavCjFGSIDc)
Author: Solvetic English

## Reporting Issues or Suggest New Features
> If you encounter any issues while using FileOrganizer or you want to suggest new features, please report them [here](https://github.com/oleksharh/FileOrganizer/issues)
> so that they can be resolved as soon as possible.
