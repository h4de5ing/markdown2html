#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import HTMLParser
from bs4 import BeautifulSoup

'''
Python版单页博客系统
author:https://github.com/h4de5ing
website:http://19code.com
blog:h4de5ing.githu.io
date:2016/07/15
'''
blog = 'h4de5ing.github.io\\'


def generateBlogFile(blog):
    '''
    file:生成html的文件名称
    title:文章的Title,显示在网页title中的内容
    date:写博客的日期
    tags:标签(多个标签用英文逗号,隔开)
    '''
    pagehtml = '''
<!DOCTYPE html>
<html>
<head>
<title>title</title>
<meta charset="UTF-8">
</head>
<body>
<xmp theme="simplex" style="display:none;">
</xmp>
<script src="v/strapdown.js"></script>
</body>
</html>
'''
    doc = 'doc\\'
    for i in os.listdir(doc):
        with open(doc + i) as f:
            for j in range(7):
                if (j == 0):
                    start = f.readline()
                elif (j == 1):
                    file = f.readline()
                elif (j == 2):
                    title = f.readline()
                elif (j == 3):
                    date = f.readline()
                elif (j == 4):
                    tags = f.readline()
                elif (j == 5):
                    end = f.readline()
                else:
                    content = f.read()
        list = [file, title, date]
        page = BeautifulSoup(pagehtml, 'lxml')
        page.title.string.replace_with(title[6:])
        page.xmp.string.replace_with(content)
        fp = open(blog + file[5:-1] + '.html', 'w+')
        str = HTMLParser.HTMLParser().unescape(page.prettify())
        fp.write(str.encode('utf-8'))
        fp.close()
    print '博客文章更新完成'


def generateIndexHtml(blog):
    index = 'index.html'
    dict = {}
    for i in os.listdir(blog):
        if i.endswith("html") & (i != index):
            page = BeautifulSoup(open(blog + i, 'r'), 'lxml')
            dict[i] = page.title.string.strip('\n').strip(' ').strip('\n')
    start = '''
<!DOCTYPE html>
<html>
 <head>
  <title>
   H4de5ing's Blog
  </title>
  <meta charset="utf-8"/>
  <base target="_blank">
 </head>
 <body>
  <xmp style="display:none;" theme="simplex">
'''
    end = '''
  </xmp>
  <script src="v/strapdown.js">
  </script>
  <div class="container">
    <div class="ds-thread" data-thread-key="home_index" data-title="h4de5ing's blog" data-url="http://19code.com"></div>
    <script type="text/javascript">
    var duoshuoQuery = {short_name:"lex109"};
    (function() {
        var ds = document.createElement('script');
        ds.type = 'text/javascript';ds.async = true;
        ds.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + '//static.duoshuo.com/embed.js';
        ds.charset = 'UTF-8';
        (document.getElementsByTagName('head')[0]
         || document.getElementsByTagName('body')[0]).appendChild(ds);
    })();
    </script>
  </div>
 </body>
</html>
'''
    i = open(blog + index, 'wb')
    i.write(start)
    for key in dict.keys():
        link = '[' + dict.get(key) + '](' + key + ')\n\r'
        i.write(link.encode('utf-8'))
    i.write(end)
    print 'index.html更新完成'


generateBlogFile(blog)
generateIndexHtml(blog)
