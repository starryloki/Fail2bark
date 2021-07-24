# Fail2bark

English

Fail2bark is an automated script that pushs Fail2ban's output information to iOS devices using Bark.

# Original Development Intention

By default, Fair2ban only has mail push service, and mail push is vulnerable to multiple conditions, which prevents it from delivering messages on time. Therefore, this script was developed to accurately push the alarm to iOS devices using iOS's APN.

# Design Ideas

+ read the incremental amount of the Fail2ban log (/var/log/fail2ban.log)

+ Match the output log with a regular expression: try and block records.

+ push the matching log to the iPhone through Bark.

  

# Useage

Refer to [Finb/Bark](https://github.com/Finb/Bark) for Bark deployment

```python
if __name__ == '__main__':
    l = Listenner()
    l.url = "https://yourserver:port/"#fill in the Park server address and port.
    l.token = "yourtoken"                 #fill in token
    l.title = "Fail2Ban Notice"           #push notification title
    l.extra = ""           #additional messages at the end
    l.readlog("/var/log/fail2ban.log")    #fail2ban log location
```

Run `python3 main.py` to run, and if you need to run in the background, you can use screen or systemd.

If you want to push only blocked messages without pushing trial messages, put `result = re.match(". *] Found. *|. *] Ban.*", line)`is replaced by `result = re.match(". *] Ban.*, line) `

# Renderings

![](https://cdn.jsdelivr.net/gh/starryloki/cdn@master/img/undmf-cs7s0.gif)

