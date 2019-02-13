#
#   Michael Cooper
#   CS3560
#   Project Euler
#


sum = 0

i = 1;

# 333 numbers divisible by 3 under 1000;
while(i <= 333):
    sum += 3 * i
    i+=1

i = 1

# 199 numbers divisible by 5 under 1000 not including 1000
while(i <= 199):
    sum += 5 * i
    i+=1

i = 1

# 66 numbers divisible by 15 under 1000; multiples of 5 OR 3 not 15
while(i <= 66):
    sum -= 15 * i
    i+=1

print("sum =",sum)
