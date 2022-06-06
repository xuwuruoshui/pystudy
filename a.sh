#!/bin/bash
x=0
y=0
for i in {125..127}
do
  ping -c 3 -i 0.2 192.168.110.$i > /dev/nul
  [ $? -eq 0 ] &&  ((x++)) ||  ((y++))
done
echo "$x条通了"
echo "$y条不通"