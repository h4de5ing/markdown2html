# Python版单页博客系统
* 网络上有许许多多的单页博客系统,为什么我还要重复造轮子呢？
* 我需要的博客系统能满足以下功能：
  - Markdown写博客
  - 能随时随地的写博客
  - 需要生成html,放在[独立博客](http://19code.com),[Github](https://h4de5ing.github.io)上

# 使用方法
* 0x00 创建博客相关的目录结构,[Clone仓库](https://github.com/h4de5ing/markdown2html/archive/master.zip)
```
│  blog.py 博客主程序
│  
├─doc  存放makrdown的目录
|     HelloWorld.md 每一篇博客就是一个markdown文件
└─h4de5ing.github.io   github博客目录,存放makrdown生成的html目录
    | HelloWorld.html 由markdown生成的html文件
    └─v               v目录用于存放html的样式文件
        │  strapdown.css
        │  strapdown.js
        │  
        └─themes
                bootstrap-responsive.min.css
                simplex.min.css
```
* 0x01 开始编写博客
在doc目录下新建一个HelloWorld.md文件,编写博客头部,不可或缺,用于标识生成的html文件名称,博客title,日期,tags等信息

```
第一行:可以留空(建议输入三个`,就是键盘上面数字键1左边的那个符号)
第二行:file:生成html的文件名称
第三行:title:文章的Title,显示在网页title中的内容
第四行:date:写博客的日期
第五行：tags:标签(多个标签用英文逗号,隔开)
第六行：可以留空(建议输入三个`,就是键盘上面数字键1左边的那个符号)
```
可以参考[markdown模板](https://github.com/h4de5ing/markdown2html/tree/master/doc)中的md文件
* 0x02 生成相应的html文件
```cmd
python blog.py
```
* 0x03 将*.github.io目录中的html文件上传至自己的仓库*.github.io仓库即可

## 感谢
[strapdown](https://github.com/arturadib/strapdown/)
