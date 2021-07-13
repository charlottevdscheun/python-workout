import glob
import threading
from queue import Queue
import time

def count_words_sequential(path: str) -> int:
    """
    Goes through each of the matching files sequentially
    """
    count = 0
    print("Sequential counting \n")
    for file in glob.glob(path):
        try:
            print(f"counting words in file: {file}")
            f = open(file, "r")
            doc = f.read().split()
            count += len(doc)
        except IsADirectoryError as e:
            print(f"There are no files to read. {e}")
            count += 0
    return count

counts = Queue()

def count_words_file(file: str) -> int:
    """
    Count the words in the file
    """
    try:
        print(f"counting words in file: {file}")
        f = open(file, "r")
        doc = f.read().split()
        words = len(doc) 
        counts.put(words)
    except IsADirectoryError as e:
        print(f"There are no files to read. {e}")
        words = 0 
    return words 

def count_words_threading(path: str) -> int:
    """
    Opens a thread for each of the files
    """
    print("Thread counting \n")
    for file in glob.glob(path):
        threading.Thread(target=count_words_file, args=(file,)).start()
    while len(threading.enumerate()) > 1:
        for t in threading.enumerate():
            if threading.current_thread() == t:
                continue
            t.join(0.1) #how long to wait before giving up
    total = 0
    while not counts.empty():
        total += counts.get()
    
    return total


first = time.time()
seq = count_words_sequential("/Users/charlotte/Documents/git/text-files/*.txt")
second = time.time()
test = count_words_threading("/Users/charlotte/Documents/git/text-files/*.txt")
third = time.time()


print(f"thr count: {test}. Took: {third - second} \n")
print(f"seq count: {seq}. Took: {second - first}\n")