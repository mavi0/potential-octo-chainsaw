#!/usr/bin/env python3

import schedule, time, os, sys, path
from config import UPDATE_INTERVAL

def clean():
    time_in_secs = time.time() - UPDATE_INTERVAL
    d = path.Path(".")
    files = d.walkfiles("*.json")

    for file in files:
        if file.mtime < time_in_secs:
            file.remove()

schedule.every(UPDATE_INTERVAL).seconds.do(clean)

while 1:
    schedule.run_pending()
    time.sleep(1)