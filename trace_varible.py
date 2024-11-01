def myNumber(number):
    if number % 2 == 1:
        myNumber = "--"+str(number)+"-"
    else:
        myNumber = "-"+str(number)+"-"
    return myNumber

x = 2
y= 6
output = ""

while x < 10:
    temp = x + y
    y = x
    x = temp
    output = output + myNumber(x)

print(output)
