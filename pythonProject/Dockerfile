FROM ubuntu:latest
LABEL authors="yyue0"

ENTRYPOINT ["top", "-b"]

# 先下载一个可以运行flask的基础镜像
FROM tiangolo/uwsgi-nginx-flask:python3.7
# 设置作者信息
MAINTAINER Serena<serena@qq.com>
# 设置工作目录
WORKDIR /app
# 将当前目录下的所有文件复制到docker引擎中的工作目录
COPY . /app
# 安装依赖
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 暴露端口
EXPOSE 5000
# 执行我们的脚本文件
CMD ["python3", "main.py","0.0.0.0","5000"]