#!/bin/sh

if [ $1 ]; then
	curl -s $1 | grep http | cut -d \" -f 2
else
	echo "Usage: ./myawesomescript <bit.ly/url>"
fi
