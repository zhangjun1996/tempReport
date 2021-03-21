import os
import time
import account
import reportTem


def userLogin(userGroup):
    tokenGroup = []  # 字典数组
    try:
        for user in userGroup:
            userAccount = account.account(user["username"], user["password"])
            userAccount.login()
            userAccount.auth()
            userAccount.getxToken()
            tokenGroup.append({"cookies": userAccount.cookies,
                               "token": userAccount.xToken})
        print("[{}]".format(time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())), "登录成功")
    except Exception as e:
        print("[{}]".format(time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())), "登录出错")
        print(e)
    return tokenGroup


def readData():
    userGroup = []  # 用户数组
    if os.getenv("USER_NAME") and os.getenv("USER_PASS"):
        print("User info found in env")
        username = os.getenv("USER_NAME")
        password = os.getenv("USER_PASS")
        user = {"username": username, "password": password}
        userGroup.append(user)
    else:
        print("User info not found in env")
        # 账号username 密码password
        user = {"username": "", "password": ""}
        userGroup.append(user)
        # return None
    return userGroup


if __name__ == '__main__':
    print("[{}]".format(time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime())), "脚本运行")
    userGroup = readData()
    tokenGroup = userLogin(userGroup)
    for account in tokenGroup:
        response = reportTem.reportTemperature(
            account["cookies"], account["token"])
        responseData = response.json()
        if responseData["code"] == 2000:
            print("[{}]".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                  "用户({})上报成功，体温36.8°C".format(responseData["data"]["name"]))
        else:
            print("[{}]".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                  "上报失败，返回信息：{}".format(responseData["msg"]))
