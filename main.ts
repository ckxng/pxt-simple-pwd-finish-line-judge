function statusRaceComplete () {
    pixel.setColor(0xffff00)
    pixel.setBrightness(255)
    console.log("race complete")
}
function pixelShowWinner (lane: number) {
    pixel.setColor(0x0000ff)
    console.log("the winner is lane " + convertToText(lane))
    while (true) {
        for (let index = 0; index < lane; index++) {
            pixel.setBrightness(255)
            control.waitMicros(500000)
            pixel.setBrightness(0)
            control.waitMicros(500000)
        }
        control.waitMicros(2000000)
    }
}
function statusInitializing () {
    pixel.setColor(0xff0000)
    pixel.setBrightness(255)
    console.log("initializing")
}
function lightSensorRead () {
    lightSensorCurrent = [pins.A1.analogRead(), pins.A2.analogRead()]
}
function lightCalibrate () {
    lightThresholdMin = [1023, 1023]
    console.log("calibrate")
    millisStartCalibrate = control.millis()
    while (control.millis() < millisStartCalibrate + 2000) {
        lightSensorRead()
        for (let index = 0; index <= lightSensorCurrent.length - 1; index++) {
            if (lightSensorCurrent[index] < lightThresholdMin[index]) {
                lightThresholdMin[index] = lightSensorCurrent[index]
            }
        }
    }
    for (let index = 0; index <= lightSensorCurrent.length - 1; index++) {
        lightThresholdMin[index] = lightThresholdMin[index] * 0.5
        console.log("lane " + (index + 1) + " is calibrated to " + lightThresholdMin[index])
    }
}
function statusReady () {
    pixel.setColor(0x00ff00)
    pixel.setBrightness(255)
    console.log("ready to race")
}
function declareWinner (lane: number) {
    statusRaceComplete()
    pixelShowWinner(lane)
}
let millisStartCalibrate = 0
let lightThresholdMin: number[] = []
let lightSensorCurrent: number[] = []
statusInitializing()
lightCalibrate()
statusReady()
forever(function () {
    lightSensorRead()
    for (let index = 0; index <= lightSensorCurrent.length - 1; index++) {
        if (lightSensorCurrent[index] < lightThresholdMin[index]) {
            declareWinner(index + 1)
        }
    }
})
