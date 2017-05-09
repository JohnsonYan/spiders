#!/usr/bin/env python2
#coding=utf-8
"""
1-2-10-9-6-5-4-3-7-8
http://www.qlcoder.com/train/spider3/1------1
http://www.qlcoder.com/train/spider3/2------2
http://www.qlcoder.com/train/spider3/3------3415
http://www.qlcoder.com/train/spider3/4------2285
http://www.qlcoder.com/train/spider3/5------1140
http://www.qlcoder.com/train/spider3/6------285
http://www.qlcoder.com/train/spider3/9------50
http://www.qlcoder.com/train/spider3/10------10
"""

import requests
import time
import threading
import Queue

class dynamicSpider(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            url = self._queue.get_nowait()
            self.spider(url)

    def spider(self, url):
        freq = self.calculateFreq(url)
        print "%s------%s" % (url, freq)

    def calculateFreq(self, url):
        freq = 0
        html_1 = requests.get(url)
        while(True):
            time.sleep(5)
            html_2 = requests.get(url)
            if(html_1.content == html_2.content):
                continue
            elif(html_1.content != html_2.content):
                print "start timer ---> %s" % url
                html_1 = html_2
                while(True):
                    time.sleep(5)
                    freq += 5
                    html_2 = requests.get(url)
                    if(html_1.content == html_2.content):
                        continue
                    elif(html_1.content != html_2.content):
                        break
            break
        return freq

def main():
    queue = Queue.Queue()
    for i in range(3,11):
        queue.put('http://www.qlcoder.com/train/spider3/'+str(i))

    threads = []
    thread_count = 5

    for i in range(thread_count):
        threads.append(dynamicSpider(queue))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
