from SHU_cxAutoSign import User

me = User()

me.user_qq = '66666666'
me.username = '11111111'
me.password = 'xxxxxxxx'
me.login()
me.loadUser()
me.getClass()
newEvent = me.getEvent()
for i in newEvent:
    type = me.getType(i["activeId"],i["courseId"],i["classId"])
    if '手势' in type:
        print('手势签到进行')
        me.gestureSign(i["activeId"],i["courseId"],i["classId"])
    if '位置' in type:
        print('位置签到进行')
        latitude,longtitude = '121.401833','31.32001'
        address = '中国上海市宝山区'
        me.locationSign(activeId=i["activeId"],latitude =latitude,longtitude=longtitude,address = address)
    if '二维码' in type:
        print('检测到二维码签到')
        enc = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
        me.QRSign(i["activeId"],enc)
    if '拍照' in type:
        print('检测到拍照签到，咱解决不了')
    if '普通' in type:
        print('普通签到,已完成')
