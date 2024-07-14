bill=int(input("Enter the bill amount:"))
sum1=0
sum2=0
while bill > 0 :
    r=bill % 10
    if r % 2==0 :
        sum1 += r
    else:
        sum2 += r
    bill=bill // 10
discount = sum1 * sum2
print(discount)