10月24日更新：数据库的jquery应与craw函数的replace的相关内容一致


# craw_train
代理ip爬取12306数据

mac下进入你自己的目录，运行如下命令即可，修改后的代码如何提交需要自己百度
git clone git@github.com:ironlionliu/craw_train.git






任务分配：

吕益行    刘尚宇     张路姚 
上海      北京      广州
深圳      天津      重庆
苏州      成都      武汉
杭州      南京      青岛
长沙      无锡      佛山
宁波      大连      郑州
烟台      东莞      沈阳
南通      泉州      唐山
济南      合肥      西安
哈尔滨     福州      长春
石家庄     徐州      常州
潍坊      温州      绍兴
盐城      扬州      鄂尔多斯
淄博      济宁      南昌
昆明      泰州      临沂
包头      台州      镇江
厦门      洛阳      嘉兴





数据库调试更改




#train_info = craw_result.json()['data']['result'][j].split('|')
#train_info : [3]:车次         [4]:该车次始发站代号  [5]:该车次终点站代号  [6]:本次查询出发站代号  
#             [7]:本次查询到达站 [8]:出发时间        [9]:到达时间         [10]:是否有票       [11]:???
#                      
#去哪网数据结构: 
'''
    {
	    "ret": true,
	    "data": {
	        "flag": true,
	        "errorCode": 0,
	        "dptStation": "北京",
	        "arrStation": "汤旺河",
	        "dptDate": "2017-06-20",
	        "s2sBeanList": [],
	        "updateTs": 1496082033,
	        "status": "UNKNOWN",
	        "dptCity": "北京",
	        "arrCity": "汤旺河",
	        "dptCityFullPy": "beijing",
	        "arrCityFullPy": "tangwanghe",
	        "transfer": false,
	        "wwwRobTicketMaxTaskNum": 20,
	        "wwwRobTicketWarmTip": "继续添加备选方案，大大提升成功率!",
	        "wwwRobTicketMaxTaskWarn": "您已选择20种抢票方案，无法继续添加",
	        "robPeriod": 30,
	        "subscribePeriod": 10,
	        "extraData": {},
	        "searchType": 0,
	        "trainSearchType": 1,
	        "recommendTrainJoint": 0,
	        "sameCity": false
	    },
	    "errmsg": "请求成功",
	    "errcode": 0
	}
	{
    'seats': {
        '无座': {
            'price': 198,
            'count': 100,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 2
            }
        },
        '硬座': {
            'price': 198,
            'count': 100,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 2
            }
        },
        '硬卧': {
            'price': 337,
            'count': 5,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 1
            }
        },
        '软卧': {
            'price': 530,
            'count': 2,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 1
            }
        }
    },
    'trainNo': 'T9',
    'trainCode': '24000000T90S',
    'dptStationName': '北京西',
    'arrStationName': '万源',
    'dptStationCode': 'BXP',
    'arrStationCode': 'WYY',
    'dptStationNo': '01',
    'arrStationNo': '11',
    'startStationName': '北京西',
    'endStationName': '重庆北',
    'startStationCode': 'BXP',
    'endStationCode': 'CUW',
    'startDate': '20170620',
    'dptTime': '15: 05',
    'arrTime': '11: 21',
    'dayDifference': '1',
    'lishiValue': '1216',
    'locationCode': 'P4',
    'saleTime': '10: 00',
    'seatTypes': '1413',
    'controlFlag': '0',
    'controlMsg': '23: 00-06: 00系统维护时间',
    'presaleDay': 0,
    'robPeriod': 0,
    'subscribePeriod': 0,
    'timeDim': 12,
    'noteDim': 34,
    'ypDim': 21,
    'saleStatus': {
        'saleId': 12,
        'desc': '可预订'
    },
    'extraBeanMap': {
        'arrDate': '2017-06-21',
        'intervalMiles': 2837,
        'sort': 0,
        'interval': '20小时16分',
        'deptStationInfo': True,
        'dptCityName': '北京',
        'deptTimeRange': '下午',
        'sale': 21,
        'startSaleTime': '2017-05-2210: 00',
        'ticketType': '硬座,
        硬卧,
        无座,
        软卧',
        'ticketsUnknown': False,
        'arriTimeRange': '上午',
        'dptDate': '2017-06-20',
        'arriStationInfo': False,
        'trainType': '空调特快',
        'arrCityName': '万源',
        'stationType': '始发,
        过路',
        'tickets': 207
    }
},
{
    'seats': {
        '无座': {
            'price': 198,
            'count': 100,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 2
            }
        },
        '硬座': {
            'price': 198,
            'count': 100,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 2
            }
        },
        '硬卧': {
            'price': 337,
            'count': 100,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 2
            }
        },
        '软卧': {
            'price': 530,
            'count': 13,
            'enable': True,
            'seatMap': {
                'ticketNumStatus': 1
            }
        }
    },
    'trainNo': 'K507',
    'trainCode': '240000K50726',
    'dptStationName': '北京西',
    'arrStationName': '万源',
    'dptStationCode': 'BXP',
    'arrStationCode': 'WYY',
    'dptStationNo': '01',
    'arrStationNo': '21',
    'startStationName': '北京西',
    'endStationName': '贵阳',
    'startStationCode': 'BXP',
    'endStationCode': 'GIW',
    'startDate': '20170620',
    'dptTime': '21: 23',
    'arrTime': '19: 57',
    'dayDifference': '1',
    'lishiValue': '1354',
    'locationCode': 'PB',
    'saleTime': '10: 00',
    'seatTypes': '1413',
    'controlFlag': '0',
    'controlMsg': '23: 00-06: 00系统维护时间',
    'presaleDay': 0,
    'robPeriod': 0,
    'subscribePeriod': 0,
    'timeDim': 12,
    'noteDim': 34,
    'ypDim': 21,
    'saleStatus': {
        'saleId': 12,
        'desc': '可预订'
    },
    'extraBeanMap': {
        'arrDate': '2017-06-21',
        'intervalMiles': 2708,
        'sort': 1,
        'interval': '22小时34分',
        'deptStationInfo': True,
        'dptCityName': '北京',
        'deptTimeRange': '晚上',
        'sale': 21,
        'startSaleTime': '2017-05-2210: 00',
        'ticketType': '硬座,
        硬卧,
        无座,
        软卧',
        'ticketsUnknown': False,
        'arriTimeRange': '晚上',
        'dptDate': '2017-06-20',
        'arriStationInfo': False,
        'trainType': '快速',
        'arrCityName': '万源',
        'stationType': '始发,
        过路',
        'tickets': 313
    }
}
'''

