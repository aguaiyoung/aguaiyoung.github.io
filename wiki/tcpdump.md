# tcpdump 命令参数

- 1.tcpdump过滤内层报文的过滤条件 VXLAN 报文：

`````` 
  inner packet 源IP10.65.128.211
  tcpdump -r 1.pcap -nn ether[0x4c:4]==0x0a4180d3
  inner packet目的IP 10.64.5.9
  tcpdump -r 1.pcap -nn ether[0x50:4]==0x0a400509
  sudo tcpdump -i eth1 udp and port 4789 and ether[0x4c:4]==0x0a4180d3 -nn
  52.39.192.163 ---120.92.128.222-- 192.191.13.16
  xgw vpc 环境 出去的给vgw网包 tcpdump -i x1 ether[0x4c:4]=0x3427c0a3 -nn 源ip 52.39.192.163
`````` 

- 2.查询lldp报文 交换机信息 


`````` 
  tcpdump -i eth0 ether proto 0x88cc -A -s0 -t -c 1 -v 

  查询lacp报文 交换机信息 

  tcpdump -i eth0 ether proto 0x8809 -A -s0 -t -c 1 -v 

`````` 

- 3.查询ospf报文 

  tcpdump -i any ip and proto 89 -nn 

- 4.查询syn报文 

`````` 
  tcpdump -i any 'tcp[tcpflags] & (tcp-syn|tcp-ack) == (tcp-syn)' -nn  
  tcpdump -i any 'tcp[13]==2' -nn   
  0000 0000 -- R R U A P R S F 【R reseverd U urgent A ack P push R rst S syn F fin】              
`````` 
- 6.查询ack报文 

  tcpdump -i any 'tcp[13]==16'  -nn

- 7.查询syn+ack报文 

  tcpdump -i any 'tcp[13]==18' -nn

- 8.查询syn报文且payload length不为0(syn+flood特征) 

  tcpdump -i any 'tcp[tcpflags] & (tcp-syn|tcp-ack) == (tcp-syn)' and '(((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)2)) != 0)' -nn 

- 9.查询lenth长度大于/小于多少的报文 

   tcpdump -i any greater 100 -nn tcpdump -i any less 100 -nn -X 看具体字段

- 10.查询指定源地址段 

  tcpdump -i any 'src net 120.132.0.0/16 or src net 123.0.0.0/8' and 'tcp[tcpflags] & (tcp-syn|tcp-ack) == (tcp-syn)' and '(((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)2)) != 0)' -nn

- 11.查询vxlan的vni报文  
  

`````` 
  tcpdump -i x1 ether[0x2e:4]==0x009c1a00 -nn 如果是-i any的话  

  tcpdump -i x1 ether[0x30:4]==0x009c1a00 -nn any多两个字节 比如vni是39962 转化成16进制就是9c1a 前后补0就行
`````` 

- 12 查询udp dns的报文 

  tcpdump -i any udp and udp[3]=0x35 -nn /tcpdump -i any udp and port=53 -nn 

- 13 查询vpc健康检查的报文 

`````` 
  抓syn 
  tcpdump -i any ether[0x30:4]==0x00fd7600 and ether[0x52:4]==0xac1b1809 and ether[0x58:2]==0x1628 -nn 
  ether[0x30:4]表示vni字段 ether[0x52:4]表示内层目的ip(fixip地址) ether[0x58:2]表示内层目的端口（监听端口）
  抓syn+ack 
  tcpdump -i any ether[0x30:4]==0x00fd7600 and ether[0x4e:4]==0xac1b1809 and ether[0x56:2]==0x1628 -nn 
  ether[0x30:4]表示vni字段 ether[0x4e:4]表示内层的源ip(fixip地址) ether[0x56:2]表示内层源端口（监听端口）

`````` 


`````` 
  亦庄对外syn包 tcpdump -i any '(src net 120.132.76.0/23 or src net 120.132.73.0/24 or src net 120.132.74.0/23 or src net 123.59.12.0/22 or src net 123.59.10.0/23 or src net 120.132.88.0/22 or src net <br/123.59.24.0/24 or src net 123.59.25.0/24 or src net 123.59.107.0/24 or src net 123.59.110.0/24 or src net 123.59.108.0/24 or src net 123.59.109.0/24 <br/or src net 106.38.199.192/27  or src net <br/111.206.115.160/27 or src net 223.71.143.96/27 or src net 123.59.27.128/25 or src net 123.59.164.0/24 or src net 123.59.165.0/24 or src net 123.59.166.0/24 or src net 123.59.167.0/24 or src net <br/120.92.2.64/26 or src net 120.92.3.0/24 or src net 120.92.2.128/25 or src net 120.92.4.0/24 or  <br/src net 120.92.5.0/24 or src net 120.92.56.0/24 or src net 120.92.57.0/24 )' and tcp[13]==0x02 -nn
  
  亦庄对外udp包 tcpdump -i any '(src net 120.132.76.0/23 or src net 120.132.73.0/24 or src net 120.132.74.0/23 or src net 123.59.12.0/22 or src net 123.59.10.0/23 or src net 120.132.88.0/22 or src net <br/123.59.24.0/24 or src net 123.59.25.0/24 or src net 123.59.107.0/24 or src net 123.59.110.0/24 or src net 123.59.108.0/24 or src net 123.59.109.0/24 <br/or src net 106.38.199.192/27  or src net <br/111.206.115.160/27 or src net 223.71.143.96/27 or src net 123.59.27.128/25 or src net 123.59.164.0/24 or src net 123.59.165.0/24 or src net 123.59.166.0/24 or src net 123.59.167.0/24 or src net <br/120.92.2.64/26 or src net 120.92.3.0/24 or src net 120.92.2.128/25 or src net 120.92.4.0/24 or  <br/ src net 120.92.5.0/24 or src net 120.92.56.0/24 or src net 120.92.57.0/24 )' and udp and port 53 -nn
  
  tcpdump -i any '(src net 120.132.76.0/23 or src net 120.132.73.0/24 or src net 120.132.74.0/23 or src net 123.59.12.0/22 or src net 123.59.10.0/23 or src net 120.132.88.0/22 or src net <br/123.59.24.0/24 or src net 123.59.25.0/24 or src net 123.59.107.0/24 or src net 123.59.110.0/24 or src net 123.59.108.0/24 or src net 123.59.109.0/24 <br/or src net 106.38.199.192/27  or src net <br/111.206.115.160/27 or src net 223.71.143.96/27 or src net 123.59.27.128/25 or src net 123.59.164.0/24 or src net 123.59.165.0/24 or src net 123.59.166.0/24 or src net 123.59.167.0/24 or src net <br/120.92.2.64/26 or src net 120.92.3.0/24 or src net 120.92.2.128/25 or src net 120.92.4.0/24 or  <br/ src net 120.92.5.0/24 or src net 120.92.56.0/24 or src net 120.92.57.0/24 )' and udp and ether[0x2c:4]=0x58585858 -nn
  
  亦庄抓包机 要在亦庄跟皂君庙同时抓 120.92部分网段在皂君庙上机器
`````` 

- 14 查询rds 6379的endpoint类型的交互报文

`````` 
  tcpdump -i any ether[0x30:4]==0x00fd7600 and '(ether[0x56:2]==0x18eb or ether[0x58:2]==0x18eb )' -nn -XX
  
  ether[0x30:4]表示vni字段 ether[0x56:2]ether[0x58:2]表示内层源和目的端口号为6379 rds基本上都是以6379为监听端

  tcpdump -i x1 dst 10.100.0.5 and '(ether[0x2e:4]==0x00fba100 or ether[0x2e:4]==0x00fcdd00)' and ether[0x56:2]==0x0cea -nn
  
  10.100.0.5 表示gxvip ether[0x56:2]==0x0cea表示目的端口是3306
`````` 

- 15 查询vm fix mac发起的报文 fa:16:3e:18:43:1c

  tcpdump -i any ether[0x30:4]==0x00fd7600 and ether[0x3c:4]==0x3e18431c -nn

- 16 根据指定mac查找落在哪台xgw上的报文
  
`````` 
  tcpdump -i eth1 ether[0x02:4]==0x9f3aa198 or ether[0x02:4]==0x9f3aa19a -nn -e -c 1 -X 
  
  (前两位mac可能有相同 尽量靠后面mac地址是唯一的) 内网的目的mac到xgw的报文 
  
  x1 ip 10.96.124.30 mac a0:36:9f:3a:a1:98 x2 ip 10.96.125.30 mac a0:36:9f:3a:a1:9a
  
  tcpdump -i eth1  -e 'ether dst a0:36:9f:3a:a1:98 or ether dst a0:36:9f:3a:a1:9a' -nn
`````` 

- 17 攻击报文 关注payload
  
`````` 
  udp payload 一般大多数会填充58585858 这种字段 全部填成0 不一定是攻击报文
  
  sudo tcpdump -i any udp and ether[0x2c:4]=0x58585858 -nn
  
  关注payload 长度为指定29
  
  tcpdump -i any udp and '((udp[4:2] -8) == 29)' -nn
`````` 

- 18 print_queue使用 

  -n  表示绑定核的队列 -q 表示 指定核所绑定的队列 比如核5idle低 就是3队列 （5-2） 2是没有绑定队列的核0和1
   
  print_queue -i x1 -n 10 -q 3

- 19 [tcpdump 抓包显示 toa 源地址](https://xiezhenye.com/2018/03/tcpdump-%E6%8A%93%E5%8C%85%E6%98%BE%E7%A4%BA-toa-%E6%BA%90%E5%9C%B0%E5%9D%80.html)

  tcpdump -nn -l "tcp dst port 1234 and ((tcp[12] & 0xf0)4)  5" 2/dev/null | \
    awk 'match($0, "Unknown Option ([0-9a-f]+)",a) {print strtonum("0x" substr(a[1],8,2)) "." strtonum("0x" substr(a[1],10,2)) "." strtonum("0x" substr(a[1],12,2)) "." strtonum("0x" substr(a[1],14,2)); fflush()}'

- 20 xor ddos包的特征值

  tcpdump -r syn_invlaid_flag.pcap 'ip[2:2]  0x50' and 'tcp[13] & 0x02 !=0' and 'tcp[20:4] == 0x020405b4' and 'tcp[24:4] == 0x01010402' -nn (syn包攻击特征)
 
  tcpdump -r syn_invlaid_flag.pcap  'udp[10:4] == 0x01200001' and 'udp[14:4] == 0x00000000' and 'udp[19] == 0x0001' -nn （dns udp攻击特征）

- 21 查询dns query请求报文
 
  tcpdump -r dns_random_udp.pcap 'ip[ip[2:2] - 3]=0x01' -nn A类型query type报文
  
  tcpdump -r dns_random_udp.pcap 'udp[udp[4:2] - 3]=0x01' -nn A类型query type报文

- 22 指定参数 -x显示16进制ip头后面 -xx显示16进制mac头后面 -X显示字符串

- 23 查询tcp datapayload特征

  tcpdump -r 1234_test.pcap '(((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)2)) != 0)' and tcp[24:4]==0x2f696d67 -nn

- 24 Chalubo botnet 包的特征值

  ls -la |awk '{print $9}'|xargs -i tcpdump -r {} src net 183.131.206.0/24  -nn
