# python_book
python2.7 test

1. 初始化目录
git init 
2. 添加文件
git add ./*
3. 提交暂存区
git commit -m "first commit"
4. 添加关联远程
git remote add origin https://github.com/warManHy/python_book.git
5. 本地和远程关联
git branch --set-upstream-to=origin/master master
6. 把远程最新的拉取下来，不合并
git fetch
7. 本地远程master分支强行合并
git pull origin master --allow-unrelated-histories
8. 提交远程
git push --set-upstream origin master