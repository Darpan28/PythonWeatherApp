import requests
import json
from tkinter import *

cityName1 = ""


def weather(cityName):
    url2 = "https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(cityName)
    response = requests.get(url2, verify=False)
    data = json.loads(response.text)

    global data1
    data1 = data["main"]["temp"]

    global data2
    data2 = data["main"]["temp_min"]

    global data3
    data3 = data["main"]["temp_max"]

    global data4
    data4 = data["main"]["humidity"]

    global data5
    data5 = data["weather"][0]["main"]


def onClickSubmit():
    global cityName1
    cityName1 = entryCity1.get()
    weather(cityName1)
    wind1.destroy()
    TempShow()

def cityWind():
    global wind1
    wind1 = Tk()

    lblTitle1 = Label(wind1, text="Weather App:")
    lblTitle1.pack()

    lblCity1 = Label(wind1, text="Enter City")
    lblCity1.pack()

    global entryCity1
    entryCity1 = Entry(wind1)
    entryCity1.pack()

    btnSubmit = Button(wind1, text="Submit", command=onClickSubmit)
    btnSubmit.pack()

    wind1.mainloop()

def TempShow():
    wind2 = Tk()

    lblTitle = Label(wind2, text="Weather App:")
    lblTitle.pack()

    global lblCity
    lblCity = Label(wind2)
    lblCity.config(text='City = ' + cityName1)
    lblCity.pack()


    global lblWeather
    lblWeather = Label(wind2)
    lblWeather.config(text='Weather = ' + str(data5))
    lblWeather.pack()

    global lblTemp
    lblTemp = Label(wind2)
    lblTemp.config(text='Temp = ' + str(data1))
    lblTemp.pack()

    global lblTempMin
    lblTempMin = Label(wind2)
    lblTempMin.config(text='Min.Temp = ' + str(data2))
    lblTempMin.pack()

    global lblTempMax
    lblTempMax = Label(wind2)
    lblTempMax.config(text='Max.Temp = ' + str(data3))
    lblTempMax.pack()

    global lblHumidity
    lblHumidity = Label(wind2)
    lblHumidity.config(text='Humdity = ' + str(data4))
    lblHumidity.pack()

    wind2.mainloop()


cityWind()