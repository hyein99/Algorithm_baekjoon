h, m = input().split()
h = int(h)
m = int(m)

mm = m - 45
hh = h
if mm < 0:
    mm = 60 + mm
    hh = hh - 1
if hh < 0:
    hh = 24 + hh
print(hh, mm)