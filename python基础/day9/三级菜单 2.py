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
print("输入任意字母可返回上一层，输入q退出")
run = True

while run:
	for k in menu:
		print('		',k)
	city = input('请输入城市：')
	if city == 'q':
		exit()
	elif city in menu:
		for x in menu.get(city):
			print('		',x)
	elif city not in menu:
		print("找不到%s，请重新输入"%(city))
		continue

	while run:
		area = input('请输入区名：')
		if area:
			if area == 'q':
				exit()
			elif area in menu[city]:
				for y in menu[city][area]:
					print('		',y)
			elif area.isalpha():
				print("返回上一层")
				break
		while run:
			place = input('请输入地名：')
			if place:
				if place == 'q':
					exit()
				elif place in menu[city][area]:
					for z in menu[city][area][place]:
						print('		',z)
						run = False
				elif place.isalpha():
					print("返回上一层")
					break





