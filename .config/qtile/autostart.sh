#!/bin/sh

# If the process doesn't exists, start one in background
run() {
	if ! pgrep $1 ; then
		$@ &
	fi
}

# Adjut montiror position and rotation
run xrandr --output DisplayPort-0 --off --output DisplayPort-1 --off --output DisplayPort-2 --primary --mode 2560x1080 --pos 1080x0 --rotate normal --output HDMI-A-0 --mode 1920x1080 --pos 0x0 --rotate right

run nitrogen --restore