import md5
import requests

def getNum(piao):
    src = '20170222JohnsonYan' + str(piao)
    for x in xrange(0,999999999):
        num = str(x)
        str1 = src + num
        start = md5.md5(str1).hexdigest()[:6]
        if start == '000000':
            return num
for piao in xrange(368,1001):
    num = getNum(piao)
    print str(piao) + ' : ' + num
    r = requests.get('http://www.qlcoder.com/train/handsomerank?_token=hWmehSeq5rACoUB3Mrv40gK3pN2c33d5ilzsLi2l&user=JohnsonYan&checkcode=' + num).text

print r
