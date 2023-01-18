# While Loop

x=0

while (x<5):
    print(x)
    x=x+1

# For Loop

for r in range(10,15):
    print(r)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days:
    print(d)


for d in days:
    if(d=="Thu"):break
    print(d)

for d in days:
    if(d=="Thu"):continue
    print(d)