# Fail2bark

English

Fail2bark 是一个将Fail2ban的输出信息使用Bark推送到iOS设备上的自动化脚本

# 开发初衷

默认情况下Fail2ban只有邮件推送服务, 而邮件推送容易受到多种条件的制约导致无法按时送达消息, 于是开发了这个脚本利用iOS的APN将警报精准推送到iOS设备

# 设计思路

+ 读取Fail2ban日志的增量(/var/log/fail2ban.log)

+ 使用正则表达式匹配输出的日志: 尝试以及封禁记录

+ 将匹配到的日志通过Bark推送到iPhone

  

# 使用

Bark的部署相关请参考[Finb/Bark](https://github.com/Finb/Bark)

```python
if __name__ == '__main__':
    l = Listenner()
    l.url = "https://yourserver:port/"    #填写Bark服务端地址以及端口
    l.token = "yourtoken"                 #填写token
    l.title = "Fail2Ban Notice"           #推送通知标题
    l.extra = ""                          #末尾的额外消息
    l.readlog("/var/log/fail2ban.log")    #fail2ban日志位置
```

运行 `python3 main.py`即可运行, 若需要后台运行, 可以使用screen或systemd

如果您希望只推送封禁消息而不推送尝试消息, 将`result = re.match(".*] Found.*|.*] Ban.*", line)`替换为`result = re.match(".*] Ban.*", line)`即可

# 效果图

![](https://cdn.jsdelivr.net/gh/starryloki/cdn@master/img/undmf-cs7s0.gif)

