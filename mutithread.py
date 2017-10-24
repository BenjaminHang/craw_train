# coding=utf-8
import threading, time, requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning) # 禁用安全请求警告

from pymongo import MongoClient
import mymod.myutil
import mymod.stableIP
from json import *



#测试并行效率
def crawtest(step, proxy, urlquery, isproxy):
    #global log1,log2
    threadname = "线程" + threading.currentThread().getName()
    headers = {"Proxy-Authorization":"SDU0Ujg4MTI4N0UxN1I2RDo4QzFERjYyNUIwMzI4ODJD"}
    http_ok = 0
    http_notok = 0
    for i in range(0,step):
        try:
            if isproxy == 1:
                craw_result = requests.get(urlquery[i]["url"],proxies=proxy,headers=headers,verify=False)
            else:
                craw_result = requests.get(urlquery[i]["url"],headers=headers,verify=False)
            if craw_result.status_code==200:
                http_ok = http_ok + 1
                #log1.write(threadname+"http_ok\n")
            else:
                http_notok = http_notok + 1
                #log1.write(threadname+"http_error\n")
		#request.get出错
        except Exception as e:
            print("sigleTest通过但线程网络请求出错"+threadname+str(e)+'\n')
            #log2.write("sigleTest通过但线程网络请求出错"+threadname+str(e)+'\n')
            break
            pass
    #log1.write("the thread is over"+threadname+'\n'+'len(http_ok)='+str(http_ok)+'\t'+'len(http_notok)='+str(http_notok)+'\n')




def craw(step, proxy, urlquery, isproxy):
    #global log1,log2
    threadname = "线程" + threading.currentThread().getName()
    #headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)","Proxy-Authorization":"SDU0Ujg4MTI4N0UxN1I2RDo4QzFERjYyNUIwMzI4ODJD"}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"}
    http_ok = 0
    http_notok = 0
    for i in range(0,step):
        try:
            if isproxy == 1:
                
                print(urlquery[i]["url"])
                craw_result = requests.get(urlquery[i]["url"],proxies=proxy,headers=headers,verify=False)
            else:
                craw_result = requests.get(urlquery[i]["url"],headers=headers,verify=False)   

            if craw_result.status_code==200:
                http_ok = http_ok + 1
				#必有正则表达式代替如此傻逼的写法
                result = craw_result.text.replace("/**/jQuery17204028351541153141_1508679375674","")
                result = result.replace("(","")
                result = result.replace(")","")
                result = result.replace(";","")
				#
                result = JSONDecoder().decode(str(result))
				#有车次
                if len(result['data']['s2sBeanList']):

                    # print(urlquery[i]["url"])
                    for train in range(0,len(result['data']['s2sBeanList'])):
                        num=result['data']['s2sBeanList'][train]["trainNo"]
                        dptstation=result['data']['s2sBeanList'][train]['dptStationName']
                        arrstation=result['data']['s2sBeanList'][train]['arrStationName']
                        startstation=result['data']['s2sBeanList'][train]['startStationName']
                        endstation=result['data']['s2sBeanList'][train]['endStationName']
                        dpttime=result['data']['s2sBeanList'][train]['dptTime']
                        arrtime=result['data']['s2sBeanList'][train]['arrTime']
                        daydiff=result['data']['s2sBeanList'][train]['dayDifference']
                        interval=result['data']['s2sBeanList'][train]['extraBeanMap']['interval']
                        intervalmiles=result['data']['s2sBeanList'][train]['extraBeanMap']['intervalMiles']
                        # print(dpttime,arrtime,daydiff,interval,intervalmiles)

                        # db.trainmap.insert_one()
                        seatdic={}
                        for seat in result['data']['s2sBeanList'][train]['seats'].keys():                        
                            price=result['data']['s2sBeanList'][train]['seats'][seat]['price']
                            seatdic[seat]=price
                        dbdata={"num":num,"dptstation":dptstation,"arrstation":arrstation,"start":startstation,\
                        "end":endstation,"dpttime":dpttime,"arrtime":arrtime,"daydiff":daydiff,"interval":interval,\
                        "intervalmiles":intervalmiles,"seats":seatdic}
                        ##本函数更新数据库
                        ##part1
                        print("有用的数据")
                        print(dbdata)
                        db.trainmap.insert_one(dbdata)
                        db.url.update({"_id":urlquery[i]["_id"]},{"$set":{"status":"hasdata"}},upsert=False,multi=False)
                        #train_data = ?????@@@于佳龙
                        #爬取后的数据处理
                        #db.trainmap.insert_one(train_data)                        
                    print(threadname+"@@@@200")
                #没车次
                else:
                    ##本函数更新数据库
                    ##part2
                    #print(threadname+"没车")
                    db.url.update({"_id":urlquery[i]["_id"]},{"$set":{"status":"nodata"}},upsert=False,multi=False)
            #非200请求，请求出错
            else:
                http_notok = http_notok + 1
                print(threadname+"@@@@"+str(craw_result.status_code))
        #request.get出错
        except Exception as e:
            # print("sigleTest通过但线程网络请求出错"+threadname+str(e)+'\n')
            #log2.write("sigleTest通过但线程网络请求出错"+threadname+str(e)+'\n')
            break
            pass
    # print("the thread is over"+threadname+'\n'+'len(http_ok)='+str(http_ok)+'\t'+'len(http_notok)='+str(http_notok)+'\n')



    
'''
		#print(craw_result.json()['data']['result'])
		if len(craw_result.json()['data']['result']):
			for j in range(0, len(craw_result.json()['data']['result'])):
				train_info = craw_result.json()['data']['result'][j].split('|')
				train_data = {"车次":train_info[3],"始发站代号":train_info[4],\
				"始发站名":english_stations[train_info[4]],\
				"终点站代号":train_info[5],\
				"终点站名":english_stations[train_info[5]],\
				"出发站代号":train_info[6],\
				"出发站名":english_stations[train_info[6]],\
				"到达站代号":train_info[7],\
				"到达站名":english_stations[train_info[7]],\
				"出发时间":train_info[8],\
				"到达时间":train_info[9]}
				db.trainmap.insert_one(train_data)
				db.url.update({"url":urlquery[i]["url"]},{"$set":{"status":"hasdata"}},\
				upsert=False, multi=False)
		else:
			db.url.update({"url":urlquery[i]["url"]},{"$set":{"status":"nodata"}},upsert=False, \
			multi=False)


'''


#测试区————测试自定义包的各种函数
'''
log1 = open("log/craw.log","w+")
log2 = open("log/crawbug.log","w+")
log3=open("log/crawttime.log","w+")
log1.write("\ncrawtest开始:\n"+str(time.ctime()))
log2.write("\ncrawtestbug开始:\n"+str(time.ctime()))
log3.write("\ncrawtesttime开始:\n"+str(time.ctime()))
start_time=time.time()

testUrl = "http://train.qunar.com/dict/open/s2s.do?"+\
        "callback=jQuery172031843804203989556_1495894108865&"+\
        "dptStation=上海&arrStation=北京&date=2017-05-31&"+\
        "type=normal&user=neibu&source=site&start=1&num=500&sort=3"

client = MongoClient()
db = client.quna
myutil = mymod.myutil.myUtil(db)
# myutil.putUrl2Mongo(372,392,2638,"2017-06-20")
myutil.updateMongo("restart")
lock = threading.Lock()
stableip = mymod.stableIP.StableIP()
proxies = stableip.getIPs("ips.py")
#craw(100,proxies[0],0)
#测试多线程速度
def callcrawtest(step, proxy, urlquery_step):
    if stableip.singleTest(proxy,testUrl):
    #if step > 0:
        print("succeded")
        crawtest(step, proxy, urlquery_step, 1)
    else:
        print("failed")

step = 1000
urlquery = list(db.url.find({"status":"no"}).limit(step*len(proxies)))
for i in range(0, step*len(proxies)):
    db.url.update({"_id":urlquery[i]["_id"]},{"$set":{"status":"ing"}},upsert=False, multi=False)

threads = []
thread_num = 0
for proxy in proxies:
    thread_num = thread_num + 1
    start = (thread_num - 1)*step
    end =(thread_num)*step
    urlquery_step = urlquery[start:end]
    onethread = threading.Thread(target = callcrawtest,args=([step,proxy,urlquery_step]),name = "name:"+str(thread_num))
    onethread.start()
    threads.append(onethread)

for thread in threads:
    thread.join()
log3.write('step='+str(step)+'\t'+'thread='+str(len(proxies))+'\n')
log3.write('time='+str(time.time()-start_time)+'\n')


log1.close()
log2.close()
log3.close()




#craw(100,proxies[0],0)
#stations = myutil.readStationsAsArr("mymod/stations.py")
#myutil.genUrl(stations,1,2,"2017-06-20")
#myutil.updateMongo("addproperty")

'''
#测试区结束



#主程序————爬虫程序
#'''

#log1 = open("log/craw.log","w+")
#log2 = open("log/crawbug.log","w+")
#log3=open("log/crawttime.log","w+")
#log1.write("\ncrawtest开始:\n"+str(time.ctime()))
#log2.write("\ncrawtestbug开始:\n"+str(time.ctime()))
#log3.write("\ncrawtesttime开始:\n"+str(time.ctime()))
start_time=time.time()

testUrl = "http://train.qunar.com/dict/open/s2s.do?"+\
        "callback=jQuery17204028351541153141_1508679375674&"+\
        "dptStation=上海&arrStation=北京&date=2017-11-11&"+\
        "type=normal&user=neibu&source=site&start=1&num=500&sort=3"

client = MongoClient()
db = client.quna
myutil = mymod.myutil.myUtil(db)
myutil.updateMongo("restart")
lock = threading.Lock()
stableip = mymod.stableIP.StableIP()
proxies = stableip.getIPs("ip1.py")
#craw(100,proxies[0],0)
def callcraw(step, proxy, urlquery_step):
    if stableip.singleTest(proxy,testUrl):
        
        craw(step, proxy, urlquery_step, 1)
    else:
        print("无效ip")
        print(proxy["http"])
        pass

step = 20
urlquery = list(db.url.find({"status":"no","from":"北京"}).limit(step*len(proxies)))

#for i in range(0, step*len(proxies)):
#    db.url.update({"_id":urlquery[i]["_id"]},{"$set":{"status":"ing"}},upsert=False, multi=False)

#threads = []
thread_num = 0
for proxy in proxies:
    thread_num = thread_num + 1
    start = (thread_num - 1)*step
    end =(thread_num)*step
    urlquery_step = urlquery[start:end]

    
    #過期之後修改日期
    # for oneUrl in urlquery_step:
    #     oneUrl["url"] = oneUrl["url"].replace("2017-06-20","2017-11-26")

    onethread = threading.Thread(target = callcraw,args=([step,proxy,urlquery_step]),name = "name:"+str(thread_num))
    onethread.start()
    #threads.append(onethread)

#for thread in threads:
#    thread.join()


#log3.write('step='+str(step)+'\t'+'thread='+str(len(proxies))+'\n')
#log3.write('time='+str(time.time()-start_time)+'\n')


#log1.close()
#log2.close()
#log3.close()

#'''
#######主函数结束







