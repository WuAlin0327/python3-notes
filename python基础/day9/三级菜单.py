menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
while True:
    print("输入q退出程序，输入其他字母返回上一层")
    province = input("请输入城市：")
    if province == 'q':
        exit()
    elif province:
        province1 = menu.get(province)
        for k in province1:
            print(k)
    area = input('请输入区:')
    if area == 'q':
        exit()
    elif area in menu[province]:
        area1 = menu[province][area]
        for k in area1:
            print(k)
    elif area.isalpha():
        area1 = menu[province]
        print("已返回上一层")
    enterprise = input("请输入地名：")
    if enterprise == 'q':
        exit()
    elif enterprise in menu[province][area]:
        enterprise1 = menu[province][area][enterprise]
        for k in enterprise1:
            print(k)
    elif enterprise.isalpha():
        enterprise1 = menu[province][area]
        print("已返回上一层")
        continue





