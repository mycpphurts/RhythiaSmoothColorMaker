# Smooth Color Generator
An easy python script to make smooth colorsets for [Rhythia](https://github.com/David20122/sound-space-plus)

## Index
- [Installing](#installing)
- [Usage](#usage)
  - [Terminology](#terminology)
- [Updating](#updating)
- [Modifying smoothness](#modifying-smoothness)

## Installing

### Required software:
- Python (and pip)
- [git for Windows](https://gitforwindows.org/) (Windows users)  [OPTIONAL]
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

### Terminology
While inside the script there's some user friendly explanations on what to do, here's some basic terminology:
- Steps: Number of lines of colors for the transition. Originally putting 50 gave you 100 (smooth in and smooth out), the math for the steps*2 changed to compensate missing colors

## Updating
If you are using git for Windows **OR** the `git` package on Linux

```sh
$ cd RhythiaSmoothColorMaker
$ git pull
```

Otherwise, download a new ZIP of the source code by pressing Code > Download ZIP
