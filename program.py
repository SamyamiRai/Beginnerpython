def sumNum(num):
    previousnumber=0
    for i in range(num):
        sum=previousnumber + i;
        print("Current Number",i,"Previous Number",previousnumber,"Sum:",sum)
        previousnumber=i

print("Program to find the sum of current number and the previous number")
print("Printing current and previous number sum in a given range(10)")
sumNum(10)

