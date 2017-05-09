#!/usr/bin/env python2
#coding=utf-8

import requests
import re
import urllib
import Queue
import threading

url = 'http://jandan.net/ooxx/page-2408'
class Jiandan_crawler(threading.Thread):
    """
    爬取煎蛋网mm图的爬虫
    """

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            url = self._queue.get_nowait()
            self.spider(url)

    def spider(self,url):
        html = requests.get(url=url)
        imgs = re.findall('<a href="//(.*?)" target="_blank" class="view_img_link">', html.content)
        for img in imgs:
            url = 'http://'+img
            name = img.split('/')[-1]
            # set a filename
            filename = '/Users/johnson/Downloads/jiandan_mm_img/'+name
            # download imgs
            urllib.urlretrieve(url, filename)
            print filename

def main():
    queue = Queue.Queue()
    # get all url from page a to b
    for i in range(2400,2411):
        queue.put('http://jandan.net/ooxx/page-'+str(i))

    threads = []
    thread_count = 10

    for i in range(thread_count):
        threads.append(Jiandan_crawler(queue))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
