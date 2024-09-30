def hamming_7_4(code: str) -> (str, str):
    # распределение данных согласно схеме декодирования
    r1 = int(code[0])
    r2 = int(code[1])
    r3 = int(code[3])
    i1 = int(code[2])
    i2 = int(code[4])
    i3 = int(code[5])
    i4 = int(code[6])

    s1 = (r1 + i1 + i2 + i4) % 2
    s2 = (r2 + i1 + i3 + i4) % 2
    s3 = (r3 + i2 + i3 + i4) % 2

    if s1 and s2 and s3:
        return f'{i1}{i2}{i3}{(not i4) * 1}', 'ошибка в бите i4'

    elif s1 and s2:
        return f'{(not i1) * 1}{i2}{i3}{i4}', 'ошибка в бите i1'

    elif s1 and s3:
        return f'{i1}{(not i2) * 1}{i3}{i4}', 'ошибка в бите i2'

    elif s2 and s3:
        return f'{i1}{i2}{(not i3) * 1}{i4}', 'ошибка в бите i3'

    return f'{i1}{i2}{i3}{i4}', 'ошибок нет или их не удалось выявить'


print(hamming_7_4('1101011'))
print(hamming_7_4('0111110'))
print(hamming_7_4('0001001'))
print(hamming_7_4('1010011'))
