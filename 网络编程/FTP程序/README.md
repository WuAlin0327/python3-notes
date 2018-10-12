### FTP作业

##### 客户端各文件夹作用：
* bin/
    * client.py    服务端
* conf/.ini 配置文件
* folder/all    客户端下用户文件保存位置
    * name/download 下载文件路径
    * name/         上传文件路径

* ftp/main.py   客户端程序入口

##### 服务端各文件夹以及各文件作用：
* bin/
    * import_conf.py    解析配置文件
    * server.py    服务端
* conf/
    * socket_conf.ini   socket配置
    * userinfo.ini   用户配置
* ftp/
    * main.py   服务端程序入口
* logger/ 保存日志（待开发）
* warehouse/ 服务器端保存文件路径
    * /name  用户保存在服务端的文件

##### 使用：
* 用户名与密码：jack,123 或者 wualin,abc

* 支持的命令操作：
    * ls /     查看当前用户目录下文件
    * get filename  从服务端用户目录下载文件到客户端用户目录下
    * put filename  从客户端用户目录上传文件到服务端用户目录下
    * cd ..     切换文件夹（待实现）


