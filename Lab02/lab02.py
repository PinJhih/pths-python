rate = float(input("請輸入利率(%):"))/100
prin = float(input("請輸入本金(萬):"))
year = int(input("請輸入時間(年):"))
total = prin * (float(1.0 + rate)**year)

print("本利和:",int(total)," 利息和:",int(total-prin))