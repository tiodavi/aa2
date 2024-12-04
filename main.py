from machine import Pin, Timer
import dht

sensor = dht.DHT11(Pin(15))

def measureTemp(self):
    sensor.measure() # 測量
    temp = sensor.temperature() # 取得溫度
    humi = sensor.humidity() # 取得濕度
    temp_humi = "%2d℃/%2d%%" % (temp, humi) # 格式代文字
    print(temp_humi)

timer1=Timer(1)
timer1.init(period=3000, mode=Timer.PERIODIC, callback=measureTemp) # 每隔3秒執行 measureTemp