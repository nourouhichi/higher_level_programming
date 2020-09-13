#!/bin/bash
#sending a json request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1" 
