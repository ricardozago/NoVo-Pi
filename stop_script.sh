#!/bin/bash

pgrep -f mopidy | awk '{print "sudo kill -9 " $1}' | sh
pgrep -f led_by_mic.py | awk '{print "sudo kill -9 " $1}' | sh

