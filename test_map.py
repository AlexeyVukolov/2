from map import Tree

map = Tree(0,0)

buffer = True
while(buffer == True):
    num = input('1: Конструктор\n'
              '2: Удаление ключа\n'
              '3: Просмотр пары\n'
              '4: Удаление всех элементов\n'
              '5: Выход\n')

    if num == '1':
            key = int(input('Введите ключ '))
            data = input('Введите данные ')
            map.add(key, data)
    elif num == '2':
            key = int(input('Введите ключ '))
            map.delete(key)
    elif num == '3':
            key = int(input('Введите ключ '))
            print(map.get(key))
    elif num == '4':
            map.clear()
    elif num == '5':
        buffer = False