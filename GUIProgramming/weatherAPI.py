#! /usr/bin/python
# coding = utf-8
import urllib.request
import json

def GetWeatherInfo():
    ApiUrl= \
            "http://api.jisuapi.com/weather/query?appkey=yourappkey&city=珠海"
    html=urllib.request.urlopen(ApiUrl)
    #读取并解码
    data=html.read().decode("utf-8")
    #将JSON编码的字符串转换回Python数据结构
    jsonArr=json.loads(data)
    #output result of json
    return jsonArr

##    if jsonArr["status"]!="0":
##        print (jsonArr["msg"])
##    result=jsonArr["result"]
##    print (result["city"],result["weather"],result["temp"],result["temphigh"],result["templow"])
