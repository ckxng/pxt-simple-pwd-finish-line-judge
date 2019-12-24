def pixelShowWinner(lane: number):
    pixel.set_color(0x0000ff)
    while True:
        for index in range(lane):
            pixel.set_brightness(255)
            control.wait_micros(500000)
            pixel.set_brightness(0)
            control.wait_micros(500000)
        control.wait_micros(2000000)
def pixelStatusRed():
    pixel.set_color(0xff0000)
    pixel.set_brightness(255)
def pixelStatusYellow():
    pixel.set_color(0xffff00)
    pixel.set_brightness(255)
def declareWinner(lane: number):
    pixelStatusYellow()
    pixelShowWinner(lane)
pixelStatusRed()
def on_forever():
    control.wait_micros(5000000)
    declareWinner(1)
forever(on_forever)