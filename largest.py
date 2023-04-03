li={1:2,3:4,6:8}
x = max(li.keys())
max = 0
for val in li.keys():
    if(val < x and val > max):
        max = val
z = li[max]
print(max,z)