from multiprocessing import Process
import os
import sqlite3

db = sqlite3.connect('test.db')
cursor = db.cursor()


stopwords = ['and', 'or', 'in', 'on', 'an', 'a', 'the', 'the', 'The','this', 'This','those','to', 'To','If','if']
def processFile(file):
    file = open(file)
    for line in file:
        words = line.split(" ")
        for word in words:
            if word not in stopwords:
                print(word)

if __name__ == '__main__':
    dirContent = os.listdir('./')
    for file in dirContent:
        if file.endswith(".txt"):
            txtFile = file
            p = Process(target=processFile, args=(txtFile,))
            p.start()
            p.join()