#coding=utf-8
from uiautomator import Device

textDidNotConn = u'\u672a\u9023\u7dda' #"未連線"
textOpenBluetooth = u'\u958b\u555f\u85cd\u7259\u529f\u80fd' #"開啟藍牙功能"
textMoreItem = u'\u66f4\u591a\u9078\u9805' #"更多選項"
textConn2Watch = u'\u9023\u7dda\u5230\u300cASUS ZenWatch\u300d' #"連線到「ASUS ZenWatch」"
textConn = u'\u5df2\u9023\u7dda' #"已連線"

dMobile = Device('FA49GWW04976') #mobile
dMobile.press.home()
#開啟 Android wear pairing app
dMobile(text="Android Wear").click.wait()

#判斷是否為已連線的狀態
if dMobile(text=textDidNotConn).exists :
    #開啟藍牙
    if dMobile(text=textOpenBluetooth).exists :    
        dMobile(text=textOpenBluetooth).click.wait()
        print '藍牙開啟成功'
    else :
        print '藍牙已開啟'


    #連接wearable
    if dMobile(description=textMoreItem).exists : 
        dMobile(description=textMoreItem).click.wait()
        dMobile(text=textConn2Watch).click()
        if dMobile(text=textConn).wait.exists(timeout=3000):
            print '手機手錶連線成功'
            
    
else:
    print '手機手錶已連線'
