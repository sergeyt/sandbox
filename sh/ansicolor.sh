#!/bin/bash

for x in {30..37}; do
    echo -e "\x1b[${x}m $x Hello world! \x1b[0m"
    echo -e "\x1b[01;${x}m 01;$x Hello world! \x1b[0m"
done
