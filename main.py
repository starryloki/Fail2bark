import time
import requests
import re


class Listenner:
    init = 0
    url = ""
    token = ""
    title = ""
    extra = ""

    def __init__(self):
        self.init = 0

    def readlog(self, log_path):
        count = 0
        position = 0
        with open(log_path, mode='r', encoding='utf8') as f1:
            while True:
                line = f1.readline().strip()
                if line:
                    count += 1
                    print("count %s line %s" % (count, line))
                    self.sent(self.compare(line))
                cur_position = f1.tell()
                if cur_position == position:
                    time.sleep(0.1)
                    self.init = 1
                    continue
                else:
                    position = cur_position
                    time.sleep(0.1)

    def compare(self, line):
        if self.init == 0:
            return None
        result = re.match(".*] Found.*|.*] Ban.*", line)
        if result:
            return line
        return None

    def sent(self, line):
        if line:
            request = requests.post(self.url + self.token + "/?title=" + self.title + "&body=" + line + self.extra)
            print(NowTime() + "Message sent! Status code = " + str(request.status_code))


def NowTime():
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    t1 = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
    str = "[ " + t1 + " ]\t"
    return str


if __name__ == '__main__':
    l = Listenner()
    l.url = "https://yourserver:port/"
    l.token = "yourtoken"
    l.title = "Fail2Ban Notice"
    l.extra = ""
    l.readlog("/var/log/fail2ban.log")
