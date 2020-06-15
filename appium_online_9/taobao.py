
import uiautomator2
import time
device = uiautomator2.connect("1181cef8")
print(device.info)
device(text="做任务，领喵币").click()
print("做任务 领喵币")
# device(text="去完成").click()
# print("去完成")
# device.press("back")
# print("返回")
# device(text="去逛逛").click()
# print("去逛逛")
# device.press("back")
# print("返回")
for i in range(27):
    print(str(i) + "次")
    time.sleep(5)
    device(text="去浏览").click()
    print("去浏览")
    time.sleep(40)
    print("浏览中...")
    device.press("back")
    print("返回")


