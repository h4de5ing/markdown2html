```
file:Git
title:Git的基本使用方法
data:2016/05/29
tags:Git
```
# 初始化你的Git
- 初次安装好git后,需要设置用户名和邮箱
```git
git config --global user.name "用户名"
git config --global user.email "邮箱"
```

## Clone 服务器代码到本地
```git
git clone git地址
```

## 创建一个本地Git版本管理仓库
```git
git init  ##初始化当前目录为git版本管理仓库
```

## 添加文件到版本管理中
```git
git add .  #添加当前目录所有改动
git add a.txt  #只添加a.txt这个文件
```

## 提交文件的改动到版本控制数据库中去
```git
git commit -m  "提交注释"
```

## 设置远程仓库地址
```git
git remote add origin 远程git地址
```

## 提交代码到远程仓库中
```git
git push -u origin master
```
