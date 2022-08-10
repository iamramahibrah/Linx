#!/bin/bash


echo -e -n "
  === Choose your OS ===
   [1] LINUX OS  
       :"
  read os
  if [[ $os == 1 ]]; then
  	python3 bin/update.py
  else
  	echo "please select "
  fi