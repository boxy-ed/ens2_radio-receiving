radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    acceleration = receivedNumber / 127.875
    led.plotBarGraph(acceleration, 8, true)
})
let acceleration = 0
radio.setGroup(45)
basic.forever(function on_forever() {
    
})
