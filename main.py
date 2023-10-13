
def on_received_number(receivedNumber):
    global acceleration
    acceleration = receivedNumber / 127.875
    led.plot_bar_graph(acceleration, 8, True)
radio.on_received_number(on_received_number)

acceleration = 0
radio.set_group(xx) 

#Set the radio group above. Use a number between 1-99

def on_forever():
    pass
basic.forever(on_forever)
