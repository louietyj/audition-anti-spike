# Audition Anti-Spike

## tl;dr

This preloads the Audition files into memory to avoid spikes when reading files not in cache.

## How to Use

Download and run the program here: [https://github.com/louietyj/audition-anti-spike/releases](https://github.com/louietyj/audition-anti-spike/releases)

If you get an "msvcr100.dll" error, [install the Microsoft 2010 C++ redistributable (x86)](http://www.microsoft.com/en-us/download/details.aspx?id=5555)

## Compilation

If you want to compile from scratch:

1. Install [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
1. Install dependencies: `py -3.4 -m pip install -r requirements.txt`
1. Compile to exe: `py -3.4 setup.py py2exe`

## License

Copyright (c) 2018 louietyj. This software is licensed under the MIT License.
