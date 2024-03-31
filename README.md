# python-trainer

## 下载
首先确认安装 Git 已经安装好，打开 cmd，切换到工作目录，输入下面的指令下载项目文件，\
`git clone git@github.com:Lucian-4a25/python-trainer.git`\
\
通过命令行切换到下载的项目下，\
`cd python-trainer`\
\
在 Github 上创建自己的仓库，命名为 python-trainer-private，然后将当前项目推送到自己的仓库，(注意替换 yourusername 为你的 github id)\
`git push git@github.com:yourusername/python-trainer.git master`\
\
删除掉当前的项目，\
`cd ..`\
`rm -rf python-trainer`\
\
使用 git 下载自己仓库的代码，(注意，替换 yourusername 为你自己的账户id)\
`git@github.com:yourusername/python-trainer.git`\
\
将当前仓库添加为名为 public 的 remote，\
`git remote add public https://github.com/Lucian-4a25/python-trainer.git`\
\
如果项目代码发生了更新，通过下面的命令拉取更新，\
`git pull public master`

## 项目
在根目录下，查看以 **project_** 为前缀的文件，以根目录下的 **project_0.py** 举例，后缀 **0** 为对应的项目序号，表示项目 **0** 的作业内容。\
\
完成每个项目，只需要编辑 **project_xx** 文件里的内容，无需对其它地方进行修改，按照项目文件中的要求完成代码的编写。

## 测试
在编写完代码后，需要验证代码的正确性，所有没有通过单元测试的代码都是不符合预期的代码。\
首先，命令行切换到 tests 目录下，如在 linux 下，\
`cd python-trainer/tests`\
\
然后在 cmd 中输入下面的命令运行单元测试，(如果测试 project_1 则只需要修改后面部分为 test_project_1.py)，\
`python3 -m unittest -v ./test_project_0.py`
