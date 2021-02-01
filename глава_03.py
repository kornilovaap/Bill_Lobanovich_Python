a = list("cat")
print(a)

a_tuple = ("one", "two", "three")
b = list(a_tuple)
print(b)

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[0][0])

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)

others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)
marxes += others
print(marxes)
marxes.append(others)
print(marxes)

marxes.insert(0, 'Gummo')
print(marxes)

del marxes[-1]
print(marxes)
del marxes[0]
print(marxes)

marxes.remove('Gummo')
print(marxes)

marxes.pop()  # автоматически ерет последний эл-т
print(marxes)
marxes.pop(0)
print(marxes)

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)

marxes = ['Groucho', 'Chico', 'Harpo']
sort_marxes = sorted(marxes)
print(sort_marxes)
print(marxes)
marxes.sort()
print(marxes)

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'Hi'
print(a, b, c, d)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)

lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]  # list with tuple
print(dict(lot))
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])  # tuple with list
print(dict(tol))
los = ['ab', 'cd', 'ef']  # list with str
print(dict(los))
tos = ('ab', 'cd', 'ef')  # tuple with str
print(dict(tos))

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
}
pythons['Gilliam'] = 'Gerry'  # вставили новое значение
print(pythons)
pythons['Gilliam'] = 'Terry'  # заменини значение ключа
print(pythons)

others = { 'Marx': 'Groucho', 'Howard': 'Moe' }
pythons.update(others)
print(pythons)

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)  # при совпадении ключей остается один ключ и его послднее значение

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
    }
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
print(marx_list[2], marx_tuple[2], marx_dict['Harpo'])

marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']
tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)
list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)
dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)

things = ["mozzarella", "cinderella", "salmonella"]
things[1].capitalize()  # Эта строка записывает слово с прописной буквы, но не меняет его в списке
things[1] = things[1].capitalize()  # Если вы хотите изменить его в списке, вам нужно присвоить его снова
things[0] = things[0].upper()
things.remove("salmonella")  # удалит элемент по значению
print(things)

surprise = ['Groucho', 'Chico', 'Harpo']
# Напишите последний элемент списка surprise со строчной буквы,
# затем обратите его и напишите с прописной буквы:
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print(surprise)

e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
# Создайте французско-английский словарь f2e на основе словаря e2f. Используйте метод items:
f2e = {}
for key, value in e2f.items():
    f2e[value]=key
print(f2e)

life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])
