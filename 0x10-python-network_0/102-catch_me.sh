#!/bin/bash
#putting
curl -sL -X PUT 0.0.0.0:5000/catch_me --data-binary "user_id=98" -H "Origin: HolbertonSchool"
