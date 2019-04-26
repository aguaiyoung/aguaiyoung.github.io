# HackTheBox （初入门槛）
## 简介
  网址 [Hack The Box :: Penetration Testing Labs](https:\\www.hackthebox.eu\)
  
  渗透测试实验室 Hack The Box是一个在线平台，允许您测试您的渗透测试技能，并与其他类似兴趣的成员交流想法和方法。

## 登录注册
   申请挑战 获取邀请码
   [Hack The Box :: Can you hack this box?](https:\\www.hackthebox.eu\invite)

## 挑战
   点击源网页代码
   
   发现有个解析js 点进去链接
   https:\\www.hackthebox.eu\js\inviteapi.min.js
   看不懂
   ``````
   eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(\^\,String)){while(c--){d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('1 i(4){h 8={"4":4};$.9({a:"7",5:"6",g:8,b:\'\d\e\n\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}1 j(){$.9({a:"7",5:"6",b:\'\d\e\k\l\m\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}',24,24,'response|function|log|console|code|dataType|json|POST|formData|ajax|type|url|success|api|invite|error|data|var|verifyInviteCode|makeInviteCode|how|to|generate|verify'.split('|'),0,{}))
   ``````
   
   导入到自己打印的html会解析成 alert 出来 看看是啥
   ``````
   function verifyInviteCode(code){var formData={"code":code};$.ajax({type:"POST",dataType:"json",data:formData,url:'\api\invite\verify',success:function(response){console.log(response)},error:function(response){console.log(response)}})}
   function makeInviteCode(){$.ajax({type:"POST",dataType:"json",url:'\api\invite\how\to\generate',success:function(response){console.log(response)},error:function(response){console.log(response)}})}
   ``````

## 加密\解密
   上面有两个函数
   
   一个是verifyInviteCode 
   
   一个是makeInviteCode
   
   既然是邀请码 那就用产生邀请码 按照他的意思来 
   
   使用post方法 产生一个邀请码
   
``````
   curl -X POST https:\\www.hackthebox.eu\api\invite\how\to\generate
   {"success":1,"data":{"data":"SW4gb3JkZXIgdG8gZ2VuZXJhdGUgdGhlIGludml0ZSBjb2RlLCBtYWtlIGEgUE9TVCByZXF1ZXN0IHRvIC9hcGkvaW52aXRlL2dlbmVyYXRl","enctype":"BASE64"},"0":200}
``````
   得到一个json格式的字符串 加密方式base64 加密出来
   
``````
   SW4gb3JkZXIgdG8gZ2VuZXJhdGUgdGhlIGludml0ZSBjb2RlLCBtYWtlIGEgUE9TVCByZXF1ZXN0IHRvIC9hcGkvaW52aXRlL2dlbmVyYXRl
   In order to generate the invite code, make a POST request to \api\invite\generate
``````
   
   有时候 会是别的加密方式 比如ROT13 
   
``````
   curl -X POST https:\\www.hackthebox.eu\api\invite\how\to\generate
   {"success":1,"data":{"data":"Va beqre gb trarengr gur vaivgr pbqr, znxr n CBFG erdhrfg gb \\ncv\\vaivgr\\trarengr","enctype":"ROT13"},"0":200}
``````
   
   那解析出来就是这样 
   
``````
   Va beqre gb trarengr gur vaivgr pbqr, znxr n CBFG erdhrfg gb \\ncv\\vaivgr\\trarengr
   In order to generate the invite code, make a POST request to \\api\\invite\\generate
``````
   
   重新再次curl
   
``````
   curl -X POST https:\\www.hackthebox.eu\api\invite\generate
   {"success":1,"data":{"code":"SUtGUUQtR0pDUkItQktHQkMtT01RVE4tQlBTQVk=","format":"encoded"},"0":200}
``````
   
  得到一个json格式 同样是加密方式base64 解密出来
  
``````
   SUtGUUQtR0pDUkItQktHQkMtT01RVE4tQlBTQVk=
   IKFQD-GJCRB-BKGBC-OMQTN-BPSAY
``````
   
## 完结
   填入邀请码后 
   
   输入相对应的用户名\邮箱 
   
   但是找不到对应提交注册按钮 
   
   按下f12 搜索一下button 再最右下脚
   
  https:\\ghostbin.com\paste\evs9b
