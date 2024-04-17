# Smooth Color Generator
An easy python script to make smooth colorsets for [Rhythia](https://github.com/David20122/sound-space-plus)

## Index
- [Installing](#installing)
- [Usage](#usage)
- [Updating]
- [Modifying smoothness](#modifying-smoothness)

## Installing

### Required software:
- Python (and pip)
- (git for Windows)[https://gitforwindows.org/] (Windows users)  [OPTIONAL]
  - You can install by pressing Code > Download ZIP
  - For my linux homies, the `git` package

```sh
$ git clone https://github.com/mycpphurts/RhythiaSmoothColorMaker.git
$ cd RhythiaSmoothColorMaker
$ pip install -r requirements.txt
```

## Usage
Inside the repository folder:

```sh
$ python Smooth.py
```

## Updating
If you are using git for Windows **OR** the `git` package on Linux

```sh
$ cd RhythiaSmoothColorMaker
$ git pull
```

Otherwise, download a new ZIP of the source code by pressing Code > Download ZIP

## Modifying smoothness
Want more lines? Read the source code! On line 13 change the number in `num_steps` to the number of lines you want (be sure to read the comment!)
