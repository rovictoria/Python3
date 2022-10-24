def new_string(symbol, count = 3):
    return symbol * count

# print(new_string('!', 5))     -> !!!!!
# print(new string('!'))     -> !!!
#print(new_string(4))     -> 12

def collection(*symbols):  # * - помогает вводить неограниченное число аргументов
    res: str = ''
    for item in symbols:
        res += item
    return res

# print(collection('a', 's', 'd', 'w')) # asdw
# print(collection('a', '1', 'd', '2')) # a1d2
# print(ccollection(1, 2, 3, 4)) # TypeError: ...

# Рекурсия
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for e in range(1, 11):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34


# Кортеж – это неизменяемый “список”
a = [3, 4]
print(a)
print(a[-1])
t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')

print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range

print(t[-2]) # green

# print(t[-200]) # IndexError: tuple index out of range

for e in t:
    print(e) # red green blue

# t[0] = 'black' # TypeError: 'tuple

t = tuple(['red', 'green', 'blue']) # список в кортеж
red, green, blue = t # кортеж в переменные  (двойное преобразование)
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue


# Словари
# Неупорядоченные коллекции произвольных
# объектов с доступом по ключу

dictionary = {}   
# \ чтобы не писать в одну строку
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента

for k in dictionary.values():
    print(k) 
# будут только значения ключей

for m in dictionary.keys():
    print(m) 
# будут сами ключи только

for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →


# Множества
# Неупорядоченная совокупность элементов

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(type(b)) # set

a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a)) # set
print(type(b)) # set
print(type(c)) # set
a = {1, 1, 1, 1, 1}
print(a) # {1}

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение множеств
i = a.intersection(b) # i = {8, 2, 5} пересечение
dl = a.difference(b) # dl = {1, 3} разница а с b
dr = b.difference(a) # dr = {13, 21} разница b с a
q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13} выполнялось по действиям: в скобках а пересечение с b,
# потом первое а объединение с b, потом разница между  объединённым и пересечённым.

# Неизменяемое множество, нельзя добавить/удалить элемент
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8)

# Списки 
list1 = [1,2,3,4,5]
list2 = list1
list2[0] = 333   #изменится и в 1, и во 2 ( аналогично для list1[0]=222)
# аккуратно с копированием данных
print(list1) # 333, 2, 3, 4, 5
print()
print(list2)
print()
print(list1.pop(2))  #удалю элемент 2 индекс, выведет его:  3
print(list1)  # [333, 2, 4, 5]
print(len(list1))

list1.insert(2,11)  # на 2 позицию поставлю число 11, без удалений др. элементов
print(list1) # вместо 4, стало 5 элементов [333, 2, 11, 4, 5]

list1.append(11) # добавить 11 в КОНЕЦ СПИСКА
print(list1) # [333, 2, 11, 4, 5, 11]