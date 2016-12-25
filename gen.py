#!/usr/bin/env python

import os
import sys
import re

print """|No|Date|Solution|Code|
|----|------|------|------|"""

for root, subdirs, files in os.walk("./"):
    for filename in files:
        path = os.path.join(root, filename)
        match = re.search(r"\.\/(\d+)-(.+)/.+py", path)
        if match:
            num = match.group(1)
            name = match.group(2)
            date = os.popen("git log --date=format:'%%Y-%%m-%%d' --format=%%ad %s | tail -1 " % path).read().rstrip()
            print "|%s|%s|[%s](https://leecode.com/problems/%s)|[Code](%s)|" % (num, date, name, name, path.split("/")[1])
