# *-* coding:utf-8 *-*
# Author：lcs

import os
import fnmatch
import tarfile
import datetime


# 匹配文件
def is_file_math(filename, patterns):
    fhttps://github.com/pingan5200/find_file.py.gitor pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True


# 循环目录
def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if is_file_math(filename, patterns):
                yield os.path.join(root, filename)
        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)


# 压缩文件
def main():
    patterns = ['*.py', '*.docx']
    now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = f"all_images_{now}.tar.gz"
    with tarfile.open(filename, 'w:gz') as f:
        for item in find_specific_files('.', patterns):
            f.add(item)

if __name__ == "__main__":
    main()
