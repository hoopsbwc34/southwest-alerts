#!/bin/bash

echo "$(date) Sleeping..."
sleep $[(RANDOM % 30)]m

echo "====== Running ========"
echo "$(date)"
/usr/bin/python3 /home/matt/southwest-alerts/southwestalerts/app.py
echo "$(date)"
echo "====== Done ========"
