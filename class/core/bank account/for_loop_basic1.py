#basic
from re import X


for x in range(0, 151):
    print(x)

#Multiples of Five
for x in range(5,1001,5):
    print(x)

#Counting, the Dojo Way
count =[]
for x in range(1, 101, 1):
        if x%5 == 0:
            count.append('Coding')
        elif x%10 == 0:
            count.append ('Coding Dojo')
        else:
            count.append(x)
print(count)

#Whoa that suckers huge
x=0
for number in range(0,500001):
    if number%2!= 0:
            x+=number
print(x)
#countdown by fours
for x in range(2018,0,-4):
    print(x)

#flexiable counter
lownum = 2
highnum = 9
mult = 3
for x in range(lownum, highnum, 1):
    if x%mult==0:
        print(x)