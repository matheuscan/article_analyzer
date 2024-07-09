from multiprocessing import Process
import os
import re


def processFile(file):
    with open(file) as f:

        for token in f.readline():
            if token != "and":
                print(token)

if __name__ == '__main__':
    dirContent = os.listdir('./')
    for file in dirContent:
        if file.endswith(".txt"):
            txtFile = file
            p = Process(target=processFile, args=txtFile)
            p.start()
            p.join()