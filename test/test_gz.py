# -*- coding:utf-8 -*-
import tarfile
import os


def main():
    filename = 'lcs.tar.gz'
    with tarfile.open(filename, 'w:gz') as f:
        for item in os.listdir('.'):
            f.add(item)


if __name__ == '__main__':
    main()
