# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
a = int(input('Введите число учащихся в 2 классе: '))
b = int(input("Введите число учащихся в 3 классе: "))
c = int(input("Введите число учащихся в 7 классе: "))
a = (a+1)//2
b = b//2+b%2
c = c//2+c%2
sum = (a + b + c) 
#res = sum //2+sum %2
print(sum)