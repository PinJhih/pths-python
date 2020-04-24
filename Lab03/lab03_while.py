def gcd( num1, num2):
  x=0
  if(num1<num2):
    x=num1
  else:
    x=num2
  while(x>0):
    if(num1%x==0):
      if(num2%x==0):
        print(num1 ,"和", num2, "的最大公因數是:", x)
        return 0
    x-=1

x = int(input("請輸入第一個數: "))
y = int(input("請輸入第二個數: "))

gcd(x,y)
  