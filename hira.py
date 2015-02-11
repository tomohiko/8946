#coding:utf-8
import hashlib

start =  ord(u'あ')
end =  ord(u'ん')

hira = []
for i in range(start, end+1, 1):
        hira.append(unichr(i).encode('utf-8'))

num = len(hira)
for i4 in range(num):
    for i3 in range(num):
        for i2 in range(num):
                for i1 in range(num):
                    msg = hira[i1] + hira[i2] + hira[i3] + hira[i4]
                            print msg,
                            print hashlib.md5(msg).hexdigest()
