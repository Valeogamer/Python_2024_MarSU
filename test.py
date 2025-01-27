u = int(input('Введите число: '))
s = 0
while u>0:
  s = s+u%10
  u = u//10
print(f"Сумма цифр числа: {s}")