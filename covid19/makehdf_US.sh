#!/bin/bash

cd /home/adivp416/public_html/covid19/

ionice -c 3 python /home/adivp416/public_html/covid19/covid19report.py dataset_US
cat /home/adivp416/public_html/covid19/reportlog.txt
