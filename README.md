# Udacity Coursework

I'm going to try and cleanup some of the Udacity intro to ML projects and port
them to py3 while I'm working on them.

## Getting Started

I've been trying to keep up with the python packaing eco-system and use pipenv,
but I'm far from an expert.  From the project root, you should be able to
install all the python dependencies:

```
pipenv install
```

N.B. matplotlib supports different output backends [1], on my ubuntu system
default was Tkinter:

```
sudo apt-get install python3-tk
```

1. https://matplotlib.org/tutorials/introductory/usage.html#what-is-a-backend

## Projects

The top level directories is the Udacity course, the subdirs are the lessons.

The main entrypoint for the project will be named main.py:

```
./main.py
```

## Datasets

If a project requires an external dataset you'll need to initialize the
project's tools module to download it.  From the project root:

```
python -m tools
```
