weight = float(input("請輸入體重(kg):"))
height = float(input("請輸入身高(cm):"))/100

bmi = weight/(height**2)

if bmi > 24:
  print("過重")
elif bmi <= 18.5:
  print("過輕")
else:
  print("適中")
