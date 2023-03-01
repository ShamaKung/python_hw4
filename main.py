#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
#(Попробуйте использовать множества и их пересечение)

'''
n=(int(input("Введите число N элементов: ")))
num_list_1=[]
for i in range(n):
    num = int(input("Введите num "))
    num_list_1.append(num)
print(num_list_1)


m=(int(input("Введите число M элементов: ")))
num_list_2 = []
for i in range(m):
    num = int(input("Введите num "))
    num_list_2.append(num)
print(num_list_2)


num_list3 = num_list_1+num_list_2

checked_nums_list = []
for i in num_list3:
    if num_list3.count(i) > 1 and i not in checked_nums_list:
        checked_nums_list.append(i)
        print(i)
'''

#В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
#Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int( input( 'n = ' ) )
lis = [ int(x) for x in input( '-> ' ).split() ]
n = len(lis)
lis = lis + lis[:2]
ma = 0
for i in range(n):
    ma = max( ma, lis[i] + lis[i+1] + lis[i+2] )
print(ma)