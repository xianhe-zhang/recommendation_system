# 推荐系统课程项目代码
本课程的代码由若干仓库构成，均已上传至课程git服务器中。      
为了方便同学们浏览，每个代码仓库都按照章节进行了分支的划分。       
如`recall-service`仓库中有`cp2`, `cp4`两个分支，就分别对应着课程第二章和第四章相应的项目代码。同时也说明第三章并没有更新这个仓库相关的代码，因此同学们可以使用前一章的代码来运行。     

## 仓库列表
- dataset
  - 课程项目数据集
- recall-service
  - 召回服务
- rank-service
  - 排序服务
- api-service
  - API接口服务
- web-service
  - 前端web网页
- feature-engineer
  - 特征处理相关代码
- flink-realtime-feature
  - Flink处理实时特征代码

## 运行整个系统
整个系统由若干模块组成，为了方便使用我这里给大家提供了一个入口脚本用来一键启动整个系统。     

**注意**: 本课程代码相关的脚本是基于Linux/Mac系统编写的，使用windows开发的同学们需要自行修改脚本进行适配。**同时强烈建议windows平台的同学通过安装虚拟机等方式用Linux进行课程项目开发**

首先大家将本仓库中的`start.sh`文件下载到本地，然后依次在`start.sh`脚本同目录下clone下面几个仓库：
- dataset
- recall-service
- rank-service
- api-service
- web-service

最终的项目目录结构如下：
```
- concrec/
    - start.sh
    - dataset/
    - recall-service/
    - rank-service/
    - api-service/
    - web-service/
```

在运行之前，大家还需要分别进入上面4个服务的目录中，切换到相应的章节分支, 如cp2分支. 并执行python虚拟环境的搭建 (本操作只需执行一次）：
- `virtualenv venv --python=python3.9`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

然后，大家打开根目录下的start.sh脚本，把dataset文件夹的**绝对路径**填到`DATASET_PATH`变量中。

之后我们就可以在根目录运行`./start.sh`脚本启动项目了，启动后可以访问`http://localhost:8080`查看运行效果。
