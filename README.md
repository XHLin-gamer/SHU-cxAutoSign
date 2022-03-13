# SHU-cxAutoSign
超星平台自动签到工具，SHU客制版!
<sub>(再也不用担心超星app犯病了)</sub>
## 样例

```python
import 

from SHU_cxAutoSign import User
me = User()
# 如果你是第一次运行，会新建资料保存文件夹
# 新建资料保存文件路径 YOUR_PACKEGES_PATH\usersData.json

me.user_qq = '66666666'
me.username = '11111111' # 学号
me.password = 'xxxxxxxx' # 密码 
# 设置用户的qq，学号，密码

me.login(me.username,me.password) #第一次先登陆

me.loadUser(me.user_q) #可以从历史记录中复活cookies，如果cookies过期则再登陆一次即可

me.getClass()
newEvent = me.getEvent()
for i in newEvent:
    type = me.getType(i["activeId"],i["courseId"],i["classId"])
    if '手势' in type:
        print('手势签到进行')
        me.gestureSign(i["activeId"],i["courseId"],i["classId"])
    if '位置' in type:
        print('位置签到进行')
        latitude,longtitude = '121.401833','31.32001'   #写入经纬度
        address = '中国上海市宝山区'                    #写入位置
        me.locationSign(activeId=i["activeId"],latitude =latitude,longtitude=longtitude,address = address)
    if '二维码' in type:
        print('检测到二维码签到')
        enc = '3BD7B5EEC7A12061217CD06A3C607C82'    #r填入二维码中的enc，静态的
        me.QRSign(i["activeId"],enc)
    if '拍照' in type:
        print('检测到拍照签到，咱解决不了')
    if '普通' in type:
        print('普通签到,已完成')
```


## 用途说明

本项目纯粹为了科研用途，为```Shu-cxAutoSign-Plugin```的工具类，enjoy it

## 安装
已发布了pipy包

```bash 
pip install SHU-cxAutoSign
```

最后`import SHU_cxAutoSign`就行了。
### 2022.3.12 去除登录模块对```selenium```的依赖
## TODO
- 简化函数接口调用方式(如果有必要)

