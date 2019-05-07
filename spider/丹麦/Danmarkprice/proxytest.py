#免费代理或不用密码的代理

import requests
url='https://medicinpriser.dk/default.aspx?lng=2'

proxy_host='80.211.36.44'
proxy_port='8080'

proxy_user=''
proxy_pass=''

proxy_meta='http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host': proxy_host,
    'port': proxy_port,
    'user': proxy_user,
    'pass': proxy_pass,
}

proxies={
    'http':proxy_meta,
    # 'https':proxy_meta
}

respones=requests.get(url,proxies=proxies)
print(respones.text)