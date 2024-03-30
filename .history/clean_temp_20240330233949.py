import os
import sys


def rmdir(path):
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            os.remove(os.path.join(path, f))
        elif os.path.isdir(os.path.join(path, f)):
            rmdir(os.path.join(path, f))
    os.rmdir(path)


def clean(dir, remove=[".history","__pycache__"]):
    for file in os.listdir(dir):
        if file in remove:
            rmdir(file)
            print("remove "+file)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        clean(sys.argv[1],sys.argv[2:])
    else:
        clean(sys.argv[1])
