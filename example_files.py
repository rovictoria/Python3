# data = open('text.txt')
# print(data)
# open - считывание файла
# print(data) -> поток данных io.TextIOWrapper name='text.txt' mode='r' encoding='cp1251 -- (кодировка, которой считывается)
# print(data.readlines())
# выведет в 2 раза больше символов из-за кодировки, на символ в 2 раза больше памяти выделяется, у нас кодировка вообще cp1251
# ['РјРѕСЂРѕР· Рё СЃРѕР»РЅС†Рµ\n', 'РґРµРЅСЊ С‡СѓРґРµСЃРЅС‹Р№']
def ReadLastRow():
    data = open('text.txt', encoding = 'utf-8')
    text = data.readlines()
# print(text)
# ['мороз и солнце\n', 'день чудесный']

    print(text[-1])
# день чудесный  (последняя строка) или длина - 1 прописать вместо [-1]
    data.close()

colors = ['red', 'green', 'yellow']
data = open('colors.txt', 'w')  #add дозаписывает после каждого запуска, write вписывает с нуля(старое удаляет, новое вписывает)
data.writelines(colors)
data.write('\ntext\n')
data.close()

#Сделать запись в файле, тогда close и не надо
with open('file.txt', 'w') as data:
    data.write('line1\n')


# Теперь как читать файл
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

#Вызов метода. Создала описание метода в отдельном файле с названием function_example
import function_example as func
print(func.f(1))