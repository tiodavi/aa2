import network
from machine import Pin
import socket

led = Pin(2, Pin.OUT)

# 連接Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('KSCU1-1', '25971684')

while not wlan.isconnected():
    pass
print('network is connected:', wlan.ifconfig())
# TEST
# 建立HTTP伺服器
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('伺服器啟動中...')

while True:
    cl, addr = s.accept()
    print('connected from', addr)
    request = cl.recv(1024)
    request = str(request)
    if '/?led=on' in request:
        led.on()
    elif '/?led=off' in request:
        led.off()
    response = """\
    HTTP/1.1 200 OK

    <html>
    <body>
    <h1>LED Panel this is https.py</h1>
    <a href="/?led=on">Open Led</a><br>
    <a href="/?led=off">Close Led</a>
    </body>
    </html>
    """
    cl.send(response)
    cl.close()

