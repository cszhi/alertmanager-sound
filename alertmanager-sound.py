# -*- coding: UTF-8 -*-
import time
import winsound
import requests,json
from time import strftime, localtime
import configparser

def count_down(t=30):
	for x in range(t,-1,-1):
	    mystr = "距离下一次检查还有" + str(x) + "秒"
	    print(mystr,end = "")
	    print("\b" * (len(mystr)*2),end = "",flush=True)
	    time.sleep(1)

def main():
	cf = configparser.ConfigParser()
	cf.read("config.ini", encoding='UTF-8')
	api = cf.get('config', 'api') #alertmanager api地址
	warn = cf.getint('config', 'warn') #0普通告警不做任何处理，1普通告警也播放告警声音
	sleep = cf.getint('config', 'sleep') #检查时间间隔

	warn_num = 0
	critical_num = 0
	message = ""
	title = " Everything is OK"
	r = requests.get(api).json()
	for alert in r:
		if alert["labels"]["severity"] == "warning":
			warn_num += 1	
		elif alert["labels"]["severity"] == "critical":
			critical_num +=1
		message = message + alert["labels"]["severity"] + ":  " + alert["annotations"]["description"] + "\n"
		
	if warn_num > 0:
		title = " 发现普通告警" if warn == 0 else " 发现普通告警，播放声音"
	if critical_num > 0:
		title = " 发现严重告警，播放声音"
		
	print("==========================================")
	print(strftime("%Y-%m-%d %H:%M:%S", localtime()) + title)
	print(message)
	
	if critical_num > 0 or (warn == 1 and warn_num > 0):
		winsound.PlaySound('alert', winsound.SND_ASYNC)
	count_down(sleep)

if __name__ == '__main__':
	while True:
		main()