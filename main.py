def statusRaceComplete():
    pixel.set_color(0xffff00)
    pixel.set_brightness(255)
    print("race complete")
def pixelShowWinner(lane: number):
    pixel.set_color(0x0000ff)
    print("the winner is lane " + convert_to_text(lane))
    while True:
        for index in range(lane):
            pixel.set_brightness(255)
            control.wait_micros(500000)
            pixel.set_brightness(0)
            control.wait_micros(500000)
        control.wait_micros(2000000)
def statusInitializing():
    pixel.set_color(0xff0000)
    pixel.set_brightness(255)
    print("initializing")
def lightSensorRead():
    lightSensorCurrent = [pins.a1.analogRead(), pins.a2.analogRead()]
def lightCalibrate():
    lightSensorRead()
    index2 = 0
    while index2 <= len(lightSensorCurrent) - 1:
        lightThresholdMin.insertAt(index2, 1023)
        index2 += 1
    print("calibrate")
    millisStartCalibrate = control.millis()
    while control.millis() < millisStartCalibrate + 2000:
        lightSensorRead()
        index3 = 0
        while index3 <= len(lightSensorCurrent) - 1:
            if lightSensorCurrent[index3] < lightThresholdMin[index3]:
                lightThresholdMin[index3] = lightSensorCurrent[index3]
            index3 += 1
    index4 = 0
    while index4 <= len(lightSensorCurrent) - 1:
        lightThresholdMin[index4] = lightThresholdMin[index4] * 0.5
        print("lane " + str((index4 + 1)) + " is calibrated to " + str(lightThresholdMin[index4]))
        index4 += 1
def statusReady():
    pixel.set_color(0x00ff00)
    pixel.set_brightness(255)
    print("ready to race")
def declareWinner(lane: number):
    statusRaceComplete()
    pixelShowWinner(lane)
millisStartCalibrate = 0
lightThresholdMin: List[number] = []
lightSensorCurrent: List[number] = []
statusInitializing()
lightCalibrate()
statusReady()
def on_forever():
    lightSensorRead()
    index5 = 0
    while index5 <= len(lightSensorCurrent) - 1:
        if lightSensorCurrent[index5] < lightThresholdMin[index5]:
            declareWinner(index5 + 1)
        index5 += 1
forever(on_forever)