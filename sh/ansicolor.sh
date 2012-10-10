#!/bin/bash

for x in {30..37}; do
    echo -e "\e[${x}m $x Hello world! \e[0m"
    echo -e "\e[01;${x}m 01;$x Hello world! \e[0m"
done
