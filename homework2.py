import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from openpyxl.workbook import Workbook

def main():
    ###合并了两个犯罪文件为一份###
    # murder=pd.read_csv("D://MyPythonSpace/homework2/murder.csv")
    # assault=pd.read_csv("D://MyPythonSpace/homework2/assault.csv")
    # file=[murder,assault]
    # train=pd.concat(file)
    # train.to_csv("crime"+".csv",index=0,sep=',')

    crime=pd.read_csv("D://MyPythonSpace/homework2/crime.csv")
    weather=pd.read_csv("D://MyPythonSpace/homework2/weather.csv")
    ###获取犯罪类型名称###
    # print(crime["Primary Type"].drop_duplicates())
    
    ###打印天气 犯罪的统计信息并保存到csv文件中###
    weather_describe=weather.describe()
    crime_describe=crime.describe()
    # print(weather_describe)
    # print(crime_describe)
    # weather_describe.to_csv('weather describe.csv',index=True)
    # crime_describe.to_csv('crime describe.csv',index=True)
    
    ###绘制2012-2013随日期变化曲线###
    weather=weather.loc[4019:4747,:]
    date_name=weather.loc[:,"Unnamed: 0"]
    temp=weather.loc[:,"Mean TemperatureF"]
    humidity=weather.loc[:," Mean Humidity"]
    dew=weather.loc[:,"MeanDew PointF"]
    # sea=weather.loc[:,"Mean Sea Level PressureIn"]
    # visibility=weather.loc[:,"Mean VisibilityMiles"]
    # wind=weather.loc[:,"Mean Wind SpeedMPH"]

    plt.figure('temperature')
    plt.plot(date_name,temp,label='temperature')
    plt.xlabel('date')
    plt.ylabel('F')
    plt.title('weather-time')
    plt.legend()

    plt.figure('humidity')
    plt.plot(date_name,humidity,label='humidity',color='red')
    plt.xlabel('date')
    plt.ylabel('y')
    plt.title('humidity-time')
    plt.legend()

    plt.figure('dew')
    plt.plot(date_name,dew,label='dew',color='green')
    plt.xlabel('date')
    plt.ylabel('y')
    plt.title('dew-time')
    plt.legend()
    plt.show()

    print(weather)





if __name__ == '__main__':
    main()
