# 🎃易知独秀-体温上报脚本
> 使用者有责任和义务保证自己上传的打卡数据真实可靠。  
> 本项目仅供学习交流使用，严禁用于其他用途! For learning and communication only, other use is strictly prohibited！  
> 作者不承担任何法律责任！The author assumes no legal liability！  
>
定时上报体温，在线自动执行
## ✨使用
>本项目使用Github Action作为你的服务器在线定时执行,安全且方便。
>
* fork该仓库到你的项目，下面都是设置你的项目
* 进入: Settings-> Secrets-> 添加USER_NAME与USER_PASS两个key, 对应value为易班info的用户名与密码 // **Important!**
![添加Secrets](https://github.com/naihaishy/TsinghuaDailyReport/blob/master/results/c.png)
* 进入: Actions 点击 Understand  // **Important!**
![Understand](https://github.com/naihaishy/TsinghuaDailyReport/blob/master/results/d.png)
* 编辑: .github/workflows/deploy.yml 随便修改点什么,例如修改时间或者加个注释，然后commit // **Important!**

**OK !**

**说明**
> 1.一定要修改deploy.xml然后commit, 系统会检测到Actions，然后加入到定时任务中，否则不会触发定时
> 
> 2.Github Actions的配置文件(.github/workflows/deploy.yml)中配置了时间 
默认是每天北京时间07:00 12:00 可以自行修改
>
> 3.Github Action服务器时间为UTC格式,比北京晚8个小时;
> 除此之外，它要慢几分钟(5分钟左右), 自己测试时多等待5分钟左右
> 
> 4.运行日志去 Action下面查看

## 👀效果图
![效果图1](https://github.com/naihaishy/TsinghuaDailyReport/blob/master/results/e.png) 
![效果图2](https://github.com/naihaishy/TsinghuaDailyReport/blob/master/results/f.png) 

## 💝感谢
[Universoar](https://github.com/Universoar/gxnu-yzdx-autoreport)   
[Naihai](https://github.com/naihaishy/TsinghuaDailyReport)  

