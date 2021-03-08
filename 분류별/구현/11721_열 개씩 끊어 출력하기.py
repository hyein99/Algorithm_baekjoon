line = input()
i = 0
while True:
    if len(line) < i+10:
        print(line[i:])
        break
    else:
        print(line[i:i+10])
        i += 10