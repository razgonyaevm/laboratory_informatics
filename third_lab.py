import re
from random import shuffle, randrange


### Начало задания на 60 баллов ###
def generate_string():
    """Генерирует строку, которую в дальнейшем можно анализировать"""
    alphabet = '1234567890qwertyuiopasdfghjklzxcvbnm{}[]\|./<>,?'
    s = ''
    for i in alphabet:
        s += i * randrange(5)
    s = list(s)
    shuffle(s)
    return ''.join(s)


def smile(string, pattern):
    """Основная программа для поиска смайликов в тексте"""
    result = re.findall(pattern, string)
    return len(result)


eyes = {0: '8', 1: ';', 2: 'X', 3: ':', 4: '=', 5: '['}
nose = {0: '-', 1: '<', 2: '-{', 3: '<{'}
mouth = {0: '(', 1: ')', 2: 'P', 3: '|', 4: '\\', 5: '/', 6: 'O', 7: '='}

isu = 467211
smile_string = eyes[isu % 6] + nose[isu % 4] + mouth[isu % 8]
smile_pattern = smile_string
if '|' in smile_pattern:
    smile_pattern = smile_pattern[:smile_pattern.index('|')] + '\\' + smile_pattern[smile_pattern.index('|'):]

elif '[' in smile_pattern:
    smile_pattern = smile_pattern[:smile_pattern.index('[')] + '\\' + smile_pattern[smile_pattern.index('['):]

elif '(' in smile_pattern:
    smile_pattern = smile_pattern[:smile_pattern.index('(')] + '\\' + smile_pattern[smile_pattern.index('('):]

elif ')' in smile_pattern:
    smile_pattern = smile_pattern[:smile_pattern.index(')')] + '\\' + smile_pattern[smile_pattern.index(')'):]

print('-' * 10)
print(smile_string)
for i in range(5):
    q = generate_string()
    for j in range(5):
        point = randrange(len(q) - len(smile_string) - 1)
        q = q[:point] + smile_string + q[point:]
        print(q, smile(q, smile_pattern))

print('-' * 10)


### Окончание задания на 60 баллов ###

### Начало задания на 18 баллов, 467211 % 6 := 3 ###
def surnames(pattern, string):
    return sorted((map(lambda x: x.split()[0], re.findall(pattern, string))))


pattern = r'([А-ЯЁ][а-яё]*|[А-ЯЁ][а-яё]*-[А-ЯЁ][а-яё]*)\s[А-ЯЁ]\.[А-ЯЁ]\.'

text1 = ('Студент Вася вспомнил, что на своей лекции Балакшин П.В. упоминал про старшекурсников, которые будут ему '
         'помогать: Анищенко А.А., Машина Е.А. и Голованова-Иванова Д.В.')
text2 = (
    'Нобелевскими лауреатами из России и СССР становились: Павлов И.П., Сенкевич Г.И., Мечников И.И., Семёнов Н.Н., '
    'Пастернак Б.Л., Черенков П.А., Тамм И.Е.')
text3 = (
    'Среди людей, становившихся людьми года по версии жунала Time, русские: Сталин И.В., Хрущёв Н.С., Андропов Ю.В., '
    'Горбачёв М.С. и Путин В.В.')
text4 = (
    'Также нобелевскими лауреатами из СССР становились Франк И.М., Ландау Л.Д., Басов Н.Г., Прохоров А.М., Шолохов М.А., '
    'Солженицын А.И., Канторович Л.В., Сахаров А.Д. и так далее')
text5 = ('Губернаторами Санкт-Петербурга в разное время были Щелканов А.А., Собчак А.А., Яковлев В.А., Беглов А.Д., '
         'Матвиенко В.И. и Полтавченко Г.С.')

for i in [text1, text2, text3, text4, text5]:
    print(surnames(pattern, i))

print('-' * 10)


### Окончание задания на 18 баллов ###

### Начало задания на 22 балла 467211 % 8 := 3###
def func(pattern, string):
    digits = re.findall(pattern, string)
    string = re.split(pattern, string)
    ans = ''
    for coin in range(len(string) - 1):
        ans += string[coin]
        ans += str(4 * int(digits[coin]) ** 2 - 7)
    return ans + string[-1]


pattern = r'-{0,1}\d+'

print(func(pattern, '20 + 22 = 42'))  # тест 1
print(func(pattern, 'sjgwrgb12dkfjbdfjb-22skjfbsfjbv234dfjbn0sojdfvn'))  # тест 2
print(func(pattern, 'dorfgnbedorg23424skjfvbn23skdjfvn234234-23 dsfgjn srg 34 34'))  # тест 3
print(func(pattern, 'dergn21342 12.3412 121 12')) # тест 4
print(func(pattern, '{]]\\`,..z/x,z.`|?><12 2323 -33 22 ---3123'))  # тест 5

### Окончание задания на 22 балла ###
