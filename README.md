# alertmanager-sound
����`python`��ʹ��`request`ģ�����`Alertmanager api`����ȡ�澯��Ϣ�����Ÿ澯������
`windows`�����С�

# ��װ
�������ذ�װ`windows`��[python](https://www.python.org/downloads/)

����������ʾ����`cd`����`python`��װ·����`Administrator`��¼�û�����ÿ���˵ĵ��Կ��ܲ�һ������Ȼ��װ`requests`ģ��

```
cd C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32
pip install requests
```

���˫������`alertmanager-sound.py`
> ���ڿ�����С���������ܹرա�

```
==========================================
2019-10-17 15:14:03 ������ͨ�澯����������
warning:  anxi Ceph״̬: HEALTH_WARN
warning:  sichuan Ceph״̬: HEALTH_WARN

==========================================
2019-10-17 15:14:35 Everything is OK


������һ�μ�黹��15��
```


# �ļ�˵��

#### �澯�����ļ�

alert.wav

#### �����ļ�

config.ini

```ini
#alertmanager api��ַ
api = http://192.168.100.1:9093/api/v2/alerts?silenced=false

#0��ͨ�澯�����κδ���1��ͨ�澯Ҳ���Ÿ澯����
warn = 1 

#���ʱ����
sleep = 30 
```

#### ������
alertmanager-sound.py

## ����
Prometheus�ĸ澯�������Ҫ����澯�����ǩ��

����ϵͳ���س��궨��Ϊ��ͨ���棨severity: warning����������ʹ���ʴ���90%Ϊ���ؾ��棨severity: critical��
```yaml
- name: system_load.rules
  rules:
  - alert: ϵͳ���س���
    expr: node_load1/count without (cpu, mode) (node_cpu_seconds_total{mode="system"})>1.1
    for: 2m
    labels:
      severity: warning
    annotations:
      summary: ϵͳ���س���
      description: '{{$labels.instance}} ��ǰ���س����� {{printf "%.2f" $value}}'

- name: partion_used.rules
  rules:
  - alert: ����ʹ���ʴ���90%
    expr: ceil(100 - ((node_filesystem_avail_bytes{fstype != "rootfs"} * 100) / node_filesystem_size_bytes{fstype != "rootfs"}))>90
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "{{$labels.mountpoint}} �����ռ����"
      description: "{{$labels.instance}} {{$labels.mountpoint}}�����ռ�ʹ���� {{$value}}%"

```
