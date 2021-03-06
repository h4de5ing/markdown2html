```
file:Tcpdump
title:tcpdump基本使用方法
date:2016/05/29
tags:Android tools,tcpdump
```
# tcpdump工具
- -i 指定网卡 any表现不限网卡 -i any,-i ech0,
- -D 列出可用网卡
- -n 不解析host
- -nn 不解析host或port
- -tttt 打印时间
- -c 接受packets数量,接受完就停止抓包
- -w 指定输出文件,文件格式为pap
- -r 从文件读取dump文件
- -s 指定每个packet中最多截取的字节数,为0时默认值262144
- -v/-vv/-vvv 指定输出详细程度,-v即可
- -e 打印数据包的数据链路层头部信息
- -E 根据加密key解密
- -A 以ASCII展示捕获的包
- -X 以Hex展示

- host ip地址或者主机名
- port 端口号
- src,dst 源或者目标(host或port)
- portrange 端口范围(10-20)
- net ip地址范围,子网掩码
- proto协议名称(tcp udp icmp)
- not 非
- and 与
- or 或

```shell
# tcudump -v -i any -s 0 -c 2000 -w /sdcard/pg.pcap
```

```shell
tcpdump host 192.168.1.1  #主机
tcpdupmp port 8080      # 端口
tcpdump src host 192.168.1.10 #源主机
tcpdump dst host 192.168.1.20  #目标主机
tcpdump src port 8080 # 源端口
tcpdump dst port 8080 #目标端口
tcpdump ortrange 20-30 #端口范围
tcpdump src portrange 20-30 #源端口范围
tcpdump dst portrange 20-30 #目标端口范围
tcpdump net 192.168.1.0/24 # 网络
tcpdump net 192.168.1.0 mask 255.255.255.0
tcpdump tcp
tcpdump not port 23   # 非
tcpdump src host 192.168.1.1 and dst port 80 # 与
tcpdump src host 192.168.1.1 or dst host 192.168.1.2

```
