#!/bin/sh

echo -n "N?"
read n

tail -n $n popular-names.txt
