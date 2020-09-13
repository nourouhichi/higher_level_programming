#!/bin/bash
#curling
curl -so /dev/null "$1" -w '%{size_download}'
