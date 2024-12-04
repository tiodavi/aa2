# 導入必要的函式庫
import machine,time  # 導入machine控制硬體和time計時模組
from machine import Pin, PWM  # 從machine模組導入Pin和PWM類別

# 主程式無限循環
while True:
    # 設定兩個LED針腳
    pin1 = Pin(23,Pin.OUT)  # 將GPIO23設為輸出模式
    pin2 = Pin(22,Pin.OUT)  # 將GPIO22設為輸出模式
    pin3 = Pin(21,Pin.OUT)  # 將GPIO22設為輸出模式
    # 初始化PWM物件
    led1 = PWM(pin1, freq=1000, duty=0)  # LED1的PWM設定:頻率1000Hz,初始工作週期0
    led2 = PWM(pin2, freq=1000, duty=0)  # LED2的PWM設定:頻率1000Hz,初始工作週期0
    led3 = PWM(pin3, freq=1000, duty=0)
    # LED控制循環
    while True:
        # LED1漸亮效果
        for i in range(0,1024,8):  # 從0到1023,每次增加8
            led1.duty(i)  # 設定LED1亮度
            time.sleep(0.01)  # 延遲0.01秒
            #print("+")  # 註解掉的除錯輸出
        
        # LED1漸暗效果
        for i in range(1023,0,-8):  # 從1023到1,每次減少8
            led1.duty(i)  # 設定LED1亮度
            time.sleep(0.01)  # 延遲0.01秒
            #print("-")  # 註解掉的除錯輸出
        
        # LED2漸亮效果
        for i in range(0,1024,8):  # 從0到1023,每次增加8
            led2.duty(i)  # 設定LED2亮度
            time.sleep(0.01)  # 延遲0.01秒
        
        # LED2漸暗效果
        for i in range(1023,0,-8):  # 從1023到1,每次減少8
            led2.duty(i)  # 設定LED2亮度
            time.sleep(0.01)  # 延遲0.01秒
        # LED3漸亮效果
        for i in range(0,1024,8):  # 從0到1023,每次增加8
            led3.duty(i)  # 設定LED2亮度
            time.sleep(0.01)  # 延遲0.01秒
        
        # LED3漸暗效果
        for i in range(1023,0,-8):  # 從1023到1,每次減少8
            led3.duty(i)  # 設定LED2亮度
            time.sleep(0.01)  # 延遲0.01秒