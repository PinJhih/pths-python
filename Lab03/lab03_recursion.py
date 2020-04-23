def gcd( num1, num2):
    if(num2 == 0):
        return num1
    else: 
        return gcd( num2, num1 % num2)

x = int(input("請輸入第一個數: "))
y = int(input("請輸入第二個數: "))

print(x ,"和", y, "的最大公因數是:", gcd(x,y))
