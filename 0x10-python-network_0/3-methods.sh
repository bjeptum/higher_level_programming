#!/bin/bash
# Display all the methods server accepts
curl -sI "$1" | awk '/Allow/{gsub(/,/,"\n"); print substr($0, index($0,$2))}' | awk 'NR>1'
