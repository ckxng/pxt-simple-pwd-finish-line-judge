# pxt-simple-2-lane-pwd-finish-line ![Build status badge](https://github.com/ckxng/pxt-simple-pwd-finish-line-judge/workflows/MakeCode/badge.svg)

## Description

This is a cheap and simple finish line judge for a two-lane pinewood derby track.

Photovoltaic sensors are installed into holes drilled into the center of each lane, and a light or LED is placed directly overhead of each sensor.  Once a car's shadow passes over one of the sensors (causing the sensed light to dim by 50%), that car will be declared the winner.  The pixel will repeatedly flash blue to indicate the winner  ("blink, 2s pause, repeat" for lane 1; "blink, blink, 2s pause, repeat" for lane 2).  Press the reset button to recalibrate and prepare for the next race.

This project was done using MakeCode to demonstrate to Cub Scouts that electronics can be useful and FUN!

## Use this extension

This repository can be added as an **extension** in MakeCode.

* open https://maker.makecode.com/
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for the URL of this repository and import

## Edit this extension

To edit this repository in MakeCode.

* open https://maker.makecode.com/
* click on **Import** then click on **Import URL**
* paste the repository URL and click import

## Blocks preview

This section shows the blocks code from the last commit in master.

![A rendered view of the blocks](https://github.com/ckxng/pxt-simple-pwd-finish-line-judge/raw/master/.makecode/blocks.png)

## Wiring Preview

This section shows the generated wiring preview:

![A rendered view of the wiring](https://github.com/ckxng/pxt-simple-pwd-finish-line-judge/raw/master/.makecode/wiring.png)

## Adding a Lane

A lane can be added by editing this function in the block editor:

    function lightSensorRead
      set lightSensorCurrent to 
        (array of 
          (analog read pin A1)
          (analog read pin A2))

Change it to:

    function lightSensorRead
      set lightSensorCurrent to 
        (array of 
          (analog read pin A1)
          (analog read pin A2)
          (analog read pin A3))

## Supported targets

* for PXT/maker
* for PXT/codal
(The metadata above is needed for package search.)

