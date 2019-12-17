# alertmanager-sound
主要实现`Prometheus Alertmanager`告警组件的告警声音。
`windows`下运行。

# 安装
下载安装`windows`版[python](https://www.python.org/downloads/)

打开命令行提示符，`cd`进入`python`安装路径（`Administrator`登录用户名，每个人的电脑可能不一样），然后安装`requests`模块

```
cd C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32
pip install requests
```

最后双击运行`alertmanager-sound.py`

```
==========================================
2019-10-17 15:14:03 发现普通告警，播放声音
warning:  anxi Ceph状态: HEALTH_WARN
warning:  sichuan Ceph状态: HEALTH_WARN

==========================================
2019-10-17 15:14:35 发现普通告警，播放声音
 Everything is OK

距离下一次检查还有15秒
```


# config.ini参数说明
```
#alertmanager api地址
api = http://192.168.100.1:9093/api/v2/alerts?silenced=false

#0普通告警不做任何处理，1普通告警也播放告警声音
warn = 1 

#检查时间间隔
sleep = 30 
```

