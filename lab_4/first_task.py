# вариант 11
# вторник, пятница
# https://itmo.ru/ru/schedule/3/153941/raspisanie_zanyatiy.htm
# xml -> yaml

with open('main_directory/main.xml') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))[1:]  # пропустим первую информационную строку

new_lines = []
for i in lines:
    if i.count('<') == 1:
        new_lines.append(i[i.index('<') + 1:i.index('>')] + ':')
    elif i.count('<') > 1:
        new_lines.append(i[i.index('<') + 1:i.index('>')] + ': ' + i[i.index('>') + 1:i.index('<', 1)])
    else:
        new_lines.append(' ')

coin = 1  # сколько отступов нужно (coin * 2)
flag = []  # флаги индексов, которым нужно в начале приписать "-"
lindex, rindex = [1], [len(new_lines) - 1]
new_new_lines = ['site:']
coin_leftshift = 0  # на сколько нужно сдвинуться влево, учитывая символ "-" и его отступ
index_space = []  # какие строчки нам нужно занулить
for i in range(1, len(new_lines)):
    if new_lines[i] and new_lines[i][-1] == ':' and new_lines[i][0] != '/':
        if new_lines[lindex[-1]:rindex[-1]].count(new_lines[i]) > 1:
            flag_remove = False  # флаг удаления лишних тегов
            for j in range(i, rindex[-1]):
                if new_lines[j] == new_lines[i]:
                    if flag_remove:
                        index_space.append(j)
                    else:
                        flag_remove = True
                    flag.append(j + 1)
        if not i in index_space:
            new_new_lines.append(' ' * 2 * coin + new_lines[i])
        rindex.append(new_lines.index(f'/{new_lines[i]}', i, rindex[-1]))
        lindex.append(i + 1)
        coin += 1
    elif new_lines[i] and new_lines[i][0] == '/':
        rindex.pop(-1)
        lindex.pop(-1)
        coin -= 1
        if coin_leftshift:
            coin_leftshift -= 1
            coin -= 1
    else:
        if not (i in flag):
            if i in index_space:
                continue
            new_new_lines.append(' ' * 2 * coin + new_lines[i])
        else:
            new_new_lines.append(' ' * 2 * coin + '- ' + new_lines[i])
            coin += 1
            coin_leftshift += 1

file = open('main_directory/file_program.yaml', 'w')
for line in new_new_lines:
    print(line, file=file)
file.close()
