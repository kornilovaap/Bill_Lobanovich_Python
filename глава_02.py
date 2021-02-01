a = 7
print(a)
b = a
print(b)
print(type(a))
print(type(b))

print(99, 'qw', 'ff gg tt')

bottles = 99
base = ''
base += 'current inventory: '  # base = base + 'current inventory: '
base += str(bottles)  # base = 'current inventory: ' + '99'
print(base)

palindrome: str = 'A man, \nA plan. \nA canal:\nPanama.'
print(palindrome)

speech = 'Today we honor our friend, the backslash: \\.'
print(speech)

start = 'Na' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbuy.'
print(start + start + middle + end)

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0], letters[1], letters[-1], letters[-2])

name = 'Henny'
print(name)
name.replace('H', 'P')
print(name)
print('P' + name[1:])

letters2 = 'abcdefghijklmnopqrstuvwxyz'
print(letters2[:])  # все символы строки
print(letters2[20:])  # с 20го и до конца строки
print(letters2[12:15])  # с 12 по 14!!
print(letters2[-3:])  # последние 3 символа
print(letters2[18:-3])  # с 18го и до 4го с конца
print(letters2[-6:-2])
print(letters2[::5])
print(letters2[4:20:3])
print(letters2[19::4])
print(letters2[:21:5])

print(letters2[::-1])  # выводит список в обратоном порядке
print(letters2[-50:])
print(letters2[:70])

print(len(letters2))

todos: str = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split())

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print("Found and signing book deals:", crypto_string)

print(letters2.startswith('abc'))
print(letters2.endswith('xwz'))
letter = 'fg'
print(letters2.find(letter))
print(letters2.count(letter))  # сколько раз встречаеся это сочетание
print(letters2.isalnum())  # являютлся ли все символы буквами или цифрами

setup = 'a duck goes into a bar...'
print(setup.strip('.'))  # удаляет нужный символ из начала и конца строки целиком
print(setup.capitalize())  # первое слово с большой буквы
print(setup.title())  # каждое слово с большой буквы
print(setup.upper())  # всё капслогом
print(setup.lower())  #
print(setup.swapcase())  # поменять регистры букв

print(setup.center(30))  # отцентровать в промежутке из 30 пробелов
print(setup.ljust(30))  # выровнять по левому краю
print(setup.rjust(30))  # выровнять по правому
