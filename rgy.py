# 導入必要的函式庫
import machine,time  # machine用於控制硬體，time用於延時控制
from machine import Pin, PWM  # 從machine導入Pin和PWM類別

# 主程式無限循環
while True:
    # 設定三個LED針腳為輸出模式
    pin1 = Pin(23,Pin.OUT)  # 將GPIO23設為輸出模式
    pin2 = Pin(22,Pin.OUT)  # 將GPIO22設為輸出模式
    pin3 = Pin(21,Pin.OUT)  # 將GPIO21設為輸出模式
    
    # 註解掉的PWM設定（未使用）
    # led1 = PWM(pin1, freq=1000, duty=0)  # LED1的PWM設定
    # led2 = PWM(pin2, freq=1000, duty=0)  # LED2的PWM設定
    # led3 = PWM()  # LED3的PWM設定（未完成）
    
    # LED2控制
    pin2.value(1)      # 打開LED1 (1=開啟)
    time.sleep(20)      # 等待20秒
    pin2.value(0)      # 關閉LED1 (0=關閉)
    
    # LED1控制
    pin1.value(1)      # 打開LED2
    time.sleep(5)      # 等待2秒
    pin1.value(0)      # 關閉LED2
    
    # LED3控制
    pin3.value(1)      # 打開LED3
    time.sleep(10)      # 等待2秒
    pin3.value(0)      # 關閉LED3