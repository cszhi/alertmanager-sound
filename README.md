# alertmanager-sound
��Ҫʵ��`Prometheus Alertmanager`�澯����ĸ澯������
`windows`�����С�

# ��װ
���ذ�װ`windows`��[python](https://www.python.org/downloads/)

����������ʾ����`cd`����`python`��װ·����`Administrator`��¼�û�����ÿ���˵ĵ��Կ��ܲ�һ������Ȼ��װ`requests`ģ��

```
cd C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32
pip install requests
```

���˫������`alertmanager-sound.py`

```
==========================================
2019-10-17 15:14:03 ������ͨ�澯����������
warning:  anxi Ceph״̬: HEALTH_WARN
warning:  sichuan Ceph״̬: HEALTH_WARN

==========================================
2019-10-17 15:14:35 ������ͨ�澯����������
 Everything is OK

������һ�μ�黹��15��
```


# config.ini����˵��
```
#alertmanager api��ַ
api = http://192.168.100.1:9093/api/v2/alerts?silenced=false

#0��ͨ�澯�����κδ���1��ͨ�澯Ҳ���Ÿ澯����
warn = 1 

#���ʱ����
sleep = 30 
```

