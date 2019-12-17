# alertmanager-sound
基于`python`，使用`request`模块调用`Alertmanager api`，获取告警信息并播放告警声音。
`windows`下运行。

# 安装
首先下载安装`windows`版[python](https://www.python.org/downloads/)

打开命令行提示符，`cd`进入`python`安装路径（`Administrator`登录用户名，每个人的电脑可能不一样），然后安装`requests`模块

```
cd C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32
pip install requests
```

最后双击运行`alertmanager-sound.py`
> 窗口可以最小化，但不能关闭。

```
==========================================
2019-10-17 15:14:03 发现普通告警，播放声音
warning:  anxi Ceph状态: HEALTH_WARN
warning:  sichuan Ceph状态: HEALTH_WARN

==========================================
2019-10-17 15:14:35 Everything is OK


距离下一次检查还有15秒
```


# 文件说明

#### 告警声音文件

alert.wav

#### 配置文件

config.ini

```ini
#alertmanager api地址
api = http://192.168.100.1:9093/api/v2/alerts?silenced=false

#0普通告警不做任何处理，1普通告警也播放告警声音
warn = 1 

#检查时间间隔
sleep = 30 
```

#### 主程序
alertmanager-sound.py

## 其他
Prometheus的告警规则里，需要定义告警级别标签。

如下系统负载超标定义为普通警告（severity: warning），根分区使用率大于90%为严重警告（severity: critical）
```yaml
- name: system_load.rules
  rules:
  - alert: 系统负载超标
    expr: node_load1/count without (cpu, mode) (node_cpu_seconds_total{mode="system"})>1.1
    for: 2m
    labels:
      severity: warning
    annotations:
      summary: 系统负载超标
      description: '{{$labels.instance}} 当前负载超标率 {{printf "%.2f" $value}}'

- name: partion_used.rules
  rules:
  - alert: 分区使用率大于90%
    expr: ceil(100 - ((node_filesystem_avail_bytes{fstype != "rootfs"} * 100) / node_filesystem_size_bytes{fstype != "rootfs"}))>90
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "{{$labels.mountpoint}} 分区空间紧张"
      description: "{{$labels.instance}} {{$labels.mountpoint}}分区空间使用率 {{$value}}%"

```
