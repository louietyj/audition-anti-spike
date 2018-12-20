import os
import textwrap
import time
import traceback
import tqdm

DEFAULT_BASEPATH = r'''C:\Program Files (x86)\Playpark\Audition Next Level'''
SUBDIRS = ['data']

PREAMBLE = textwrap.dedent('''
    Audition Anti-Spike
    Latest version: https://github.com/louietyj/audition-anti-spike
''').strip()

LICENSE = textwrap.dedent('''
    MIT License

    Copyright (c) 2018 louietyj

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
''').strip()

def get_file_paths(basepath):
    file_paths = []
    for subdir in SUBDIRS:
        for file in os.listdir(os.path.join(basepath, subdir)):
            path = os.path.join(basepath, subdir, file)
            if os.path.isfile(path):
                file_paths.append(path)
    return file_paths

def main():
    print(PREAMBLE)
    print('\n' + '=' * 80 + '\n')
    print(LICENSE)
    print('\n' + '=' * 80 + '\n')
    while True:
        try:
            basepath = input('Enter your Audition directory or leave blank for default: ') or DEFAULT_BASEPATH
            filepaths = get_file_paths(basepath)
            break
        except FileNotFoundError:
            print('Invalid directory: %s' % basepath)
    total_size = sum(map(os.path.getsize, filepaths))
    print('Base path: %s' % basepath)
    print('%s files found, total size %s GB' % (len(filepaths), round(total_size / 2**30, 2)))
    for path in tqdm.tqdm(filepaths, desc='Preloading files'):
        with open(path, 'rb') as handle:
            _ = handle.read()
    print('You can now start Audition. This window will close in 3 seconds.')
    time.sleep(3)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        while True:
            time.sleep(60)
