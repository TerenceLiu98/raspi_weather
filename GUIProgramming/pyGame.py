#encoding: utf-8
import pygame
import time
import weatherAPI # It is coded by lee in weatherAPI.py

def ShowPicture(picturepath,x0,y0):  
    background=pygame.image.load(picturepath)
    background.convert_alpha()
    window.blit(background,(x0,y0))
    return
def ShowCircle():
    pygame.draw.circle(window,pygame.Color(255,255,255),(width/2,height/2),radius,fill)
    return
def ShowLine(x0,y0,x1,y1):
    pygame.draw.line(window,pygame.Color(255,255,255),(x0,y0),(x1,y1),fill)
    return                               
def ShowRec(x0,y0,x1,y1):
    pygame.draw.rect(window,pygame.Color(255,255,255),(x0,y0,x1,y1),fill)
    return  
def ShowStr(mystring,x0,y0,size):
    font=pygame.font.Font('/home/pi/LeeFolder/GUIProgramming/gkai00mp.ttf',size,bold=1)
    textSuface=font.render(mystring,1,pygame.Color(255,255,255))
    window.blit(textSuface,(x0,y0))                    
    return
#背景参数设置                            
width=800
height=600
radius=100
fill=1
#初始化背景
pygame.init()
#window=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
window=pygame.display.set_mode((width,height))
window.fill(pygame.Color(255,255,255))

loop=0
while True:
    window.fill(pygame.Color(0,0,0))
   # ShowPicture("a_3.gif",20,450)
    #draw grids
    ShowStr(u"时间",10,20,64)
    ShowRec(10,10,780,580)
    ShowLine(10,100,790,100)
    ShowLine(10,300,790,300)
    ShowLine(400,100,400,590)
    ShowLine(205,300,205,590)
    ShowLine(605,300,605,590)
    #time show
    mylocaltime=time.localtime()
    myclock=time.strftime("%H:%M:%S %Y-%m-%d",mylocaltime)#13:15:03 2017-04-21
    ShowStr(myclock,150,20,64)
    mytime=time.strftime("%A",mylocaltime)#Thursday
    ShowStr(mytime,650,75,24)
    #weather show
    if loop % 10800==0 : #update per 3 hours
        jsonArr=weatherAPI.GetWeatherInfo()
        if jsonArr["status"]!="0":
            print (jsonArr["msg"])
        result=jsonArr["result"]
        print (result["city"],result["weather"],result["temp"],result["temphigh"],result["templow"])
        AQI=result["aqi"]
        index=result["index"]
        index0=index[0]
        daily=result["daily"]
        day1=daily[1]#明天天气预报
        day2=daily[2]#明天天气预报
        day3=daily[3]#明天天气预报
        day4=daily[4]#明天天气预报
        #记录请求数据时间
        updatingtime=time.strftime("%H:%M:%S",mylocaltime)#Thursday
    #室外温湿度
    ShowPicture("pictures/"+result["img"]+".png",50,130)
    ShowStr(result["city"],20,110,24)
    ShowStr(result["weather"],20,220,64)
    ShowStr(result["temp"]+"℃",170,100,120)
    ShowStr("最高"+result["temphigh"]+"℃"+" "+"最低"+result["templow"]+"℃",170,210,26)
    ShowStr(result["humidity"]+"%",220,230,70)
    ShowStr(result["winddirect"],410,120,64)
    ShowStr(result["windpower"],480,200,32)
    #空气质量
    ShowStr(AQI["pm2_5"],600,100,120)
    ShowStr("PM2.5:"+AQI["quality"],600,210,20)
    ShowStr(index0["detail"],420,250,20)
    #未来几天天气预报
    ShowStr(day1["date"],45,310,24)
    ShowStr(day1["day"]["weather"],45,450,64)
    ShowStr(day1["day"]["windpower"],140,360,24)
    ShowStr(day1["night"]["templow"]+"~"+day1["day"]["temphigh"]+"℃",40,550,32)
    ShowPicture("pictures/"+day1["day"]["img"]+".png",60,360)

    ShowStr(day2["date"],245,310,24)
    ShowStr(day2["day"]["weather"],245,450,64)
    ShowStr(day2["day"]["windpower"],340,360,24)
    ShowStr(day2["night"]["templow"]+"~"+day2["day"]["temphigh"]+"℃",240,550,32)
    ShowPicture("pictures/"+day2["day"]["img"]+".png",260,360)

    ShowStr(day3["date"],445,310,24)
    ShowStr(day3["day"]["weather"],445,450,64)
    ShowStr(day3["day"]["windpower"],540,360,24)
    ShowStr(day3["night"]["templow"]+"~"+day2["day"]["temphigh"]+"℃",440,550,32)
    ShowPicture("pictures/"+day3["day"]["img"]+".png",460,360)
    
    ShowStr(day4["date"],645,310,24)
    ShowStr(day4["day"]["weather"],645,450,64)
    ShowStr(day4["day"]["windpower"],740,360,24)
    ShowStr(day4["night"]["templow"]+"~"+day2["day"]["temphigh"]+"℃",640,550,32)
    ShowPicture("pictures/"+day4["day"]["img"]+".png",660,360)

    #记录请求数据时间
    ShowStr("Last update:"+updatingtime,600,280,18)
    
    #update 
    pygame.display.update()
    time.sleep(1)
    loop +=1
    #全屏
   #for event in pygame.event.get():
   #     if event.type==pygame.KEYDOWN:
   #         running=False
#pygame.quit()
