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