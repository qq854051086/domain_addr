# coding:utf-8
import os
import win32clipboard as w
import win32con
import re
import requests
# #执行测试当前环境是否具有网络
#请复制示例内容:https://www.baidu.com/ （开头必须为http或https）

def walk_cmd(command_word,status):
    command_result = os.popen('ping %s'%command_word).readlines()
    for line in command_result:
        ip_addr = re.findall('\[(.*?)\]',line)
        if ip_addr:
            if status == 200:
                print('网络链接正常')
                return True
            print('获取到的IP:', ip_addr[0])
            return ip_addr

#查询最后一次剪切板内容，进行执行获取IP

def gettext():
    w.OpenClipboard()
    board = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()

    print('剪切板内容',board)
    try:
        if re.findall('http',board.decode('utf-8')):   #判断是否为URL链接
            return board.decode('utf-8').split('/')[2]
        else:
            print('不是有效的URL')
            return False
    except:
        print('不是有效的URL')
        return False

def get_ip_addr(ip):
    url = 'http://www.ip138.com/ips138.asp?ip=%s&action=2' % ip[0]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36', }
    response = requests.get(url, headers=headers)
    print('查询地理位置返回状态码：%s' % str(response.status_code))
    if response.status_code == 200:
        re_result = re.findall('<li>本站数据：(.*?)</li>', str(response.content.decode('gb2312')))
        print(re_result[0])
    else:
        print('查询受限~~')

def main():
    walk_cmd('www.baidu.com',200)
    match_result = gettext()
    if match_result:
        get_ip_addr(walk_cmd(match_result,201))

main()