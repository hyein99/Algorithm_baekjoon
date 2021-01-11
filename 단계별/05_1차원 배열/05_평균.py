n = int(input())
gd = list(map(int, input().split()))
ngd = [i/max(gd)*100 for i in gd]
print(sum(ngd)/len(ngd))