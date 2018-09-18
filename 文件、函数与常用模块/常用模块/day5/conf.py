"""
1.修改时区 default-time-zone = '+8:00' 为 校准的全球时间 +00:00
2.删除 explicit_defaults_for_timestamp = true
3.为DEFAULT增加一条 character-set-server = utf8
"""

import configparser

config = configparser.ConfigParser()
config.read("conf.cnf")
sec = config.remove_option('mysqld','explicit_defaults_for_timestamp')
config.set('DEFAULT','character-set-server','utf-8')
config.set('mysqld','default-time-zone','+00:00')
config.write(open("conf.cnf",'w'))
