### Client:
    * bin/start.py 程序入口
    * conf/配置文件存放
    * core/
        * auth.py 登陆，注册以及上传下载查看当前文件夹下文件以及删除功能存放
        * cline.py 与服务端通信
    * home 本地用户目录
    
    
### Server：
    * bin/start.py程序入口
    * conf
        * user_pick/客户端保存在服务端的账号信息
        * userinfo/用户账号密码保存
        * setting/配置文件
    * core
        * auth.py 用户登陆注册功能模块
        * server.py 服务端，支持多线程与queue，上传下载删除等功能存放模块
        * user.py  用户对象保存模块
        
    * home
        * 用户在服务端的文件夹
        
    * logger 还没实现
    
* 已实现功能：
    * 支持多并发
    * 实现线程池Queue
    * 允许配置最大并发数：conf/setting/thread_size
    
* 用户账号密码：
    * wualin,123
    * tom,123
    * 也可以自己注册
    