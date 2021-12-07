import re
import requests
import os

domain_dict = {
    "github.com": "https://github.com.ipaddress.com/",
    "assets-cdn.github.com": "https://github.com.ipaddress.com/assets-cdn.github.com",
    "github.global.ssl.fastly.net": "https://fastly.net.ipaddress.com/github.global.ssl.fastly.net"
}
hosts_dict = {}

for domain, url in domain_dict.items():
    method = "GET"
    req = requests.request(method=method, url=url)
    pattern = r'<th>IPv4 Addresses</th><td><ul class="comma-separated"><li>(.+?)</li>'
    com = re.compile(pattern)
    ip = com.findall(req.content.decode())[0]
    hosts_dict[ip] = domain

hosts_path_dict = {
            "nt": "c:\\windows\\system32\\drivers\\etc\\hosts",
            "posix": "/etc/hosts"}
hosts_path = hosts_path_dict.get(os.name)
print ("\nhosts:", hosts_path, "\n")

for k,v in hosts_dict.item():
    print (k,v)
#print ("\n".join([f"{k} {v}" for k, v in hosts_dict.items()]))
