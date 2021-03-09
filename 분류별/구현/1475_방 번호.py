from collections import Counter
import sys

c = Counter(sys.stdin.readline())

x = c['9']+c['6']
c['9'] = x//2
c['6'] = x-c['9']
print(max(c.values()))