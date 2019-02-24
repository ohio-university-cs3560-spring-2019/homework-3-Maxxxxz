#!/bin/bash

#
#	Michael Cooper
#	Ohio University CS3560
#	count.sh
#	calls count.py, sending it the script's current directory
#

dir=$(pwd)

python count.py $dir