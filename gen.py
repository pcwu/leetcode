#!/usr/bin/env python

import os
import sys
import re

print """LeetCode Practice
=====================

*   [My LeetCode Profile](https://leetcode.com/pcwu7/)

|No|Date|Code|Problem|
|----|------|------|------|"""

for root, subdirs, files in os.walk("./"):
    for filename in files:
        path = os.path.join(root, filename)
        match = re.search(r"\.\/(\d+)-(.+)/(.+[py|js])", path)
        if match:
            num = match.group(1)
            name = match.group(2)
            code = match.group(3)
            date = os.popen("git log --date=format:'%%Y-%%m-%%d' --format=%%ad %s | tail -1 " % path).read().rstrip()
            print "|%s|%s|[%s](%s/)|[%s](https://leetcode.com/problems/%s/)|" % (num, date, code, path.split("/")[1], name, name)
