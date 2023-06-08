import os
import json

def opener():
    with open('__pycache__/objects.cpython-310.pyc', 'rb') as f:
        a = f.read()
    print(type(a))

#if __name__ == 'main':
opener()
