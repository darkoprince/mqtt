from gpiozero import LED
from time import sleep
import paho.mqtt.client as mqtt



led = LED(17)


def dot():
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)

def dash():
        led.on()
        sleep(1)
        led.off()
        sleep(1)
     

def p():
        dot()
        dash()
        dash()
        dot()

def r():
        dot()
        dash()
        dot()
def i():
        dot()
        dot()
def n():
        dash()
        dot()
def c():
        dash()
        dot()
        dash()
        dot()
def e():
        dot()



def say_my_name():
        p()
        r()
        i()
        n()
        c()
        e()

def on_message(client, userdata, message):
        print message.payload
	say_my_name()
	

def on_connect(client, userdata, flags, code):
        print "connected:" + str(code)
        client.subscribe("test/all")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('moorhouseassociates.com', 1883, 60)

client.loop_forever()

