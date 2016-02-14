import sys
i=0
for arg in sys.argv:
    if len(arg)%3==0:
        i+=1
print(i)
