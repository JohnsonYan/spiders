#!/usr/bin/env python2
#coding=utf-8

import requests
import threading
import Queue
from bs4 import BeautifulSoup as bs

headers = {
xxx
}


class SeeBugPoc(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            url = self._queue.get_nowait()

    def spider(self, url):
        html = requests.get(url=url, headers=headers)

def main():
    queue = Queue.Queue()
    for i in range(1,6):
        queue.put('xxxx'+str(i))

    threads = []
    thread_count = 1

    for i in range(thread_count):
        threads.append(SeeBugPoc(queue))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
