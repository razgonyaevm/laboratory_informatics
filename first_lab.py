from string import ascii_uppercase, digits
from fractions import Fraction
from math import factorial

ALPHABET = digits + ascii_uppercase
FIB_ALPHABET = [1, 2]

# генерация алфавита системы счисления Цекендорфа
for i in range(1000):
    FIB_ALPHABET.append(FIB_ALPHABET[-1] + FIB_ALPHABET[-2])


def convert_to_ten(numb: str, base_from) -> float:
    # перевод для числовых систем счисления
    if type(base_from) == int:
        # проверка, является ли число целым или десятичной дробью
        if '.' in numb:
            coin = numb.index('.')
            real = numb[:coin]
            img = numb[coin + 1:]
        else:
            real = numb
            img = ''

        # переводим целую часть числа
        coin = 0
        ans_real = 0
        for i in range(len(real) - 1, -1, -1):
            ans_real += ALPHABET.index(real[i]) * base_from ** coin
            coin += 1

        # переводим часть числа после точки (для точности вычислений будем использовать библиотеку fractions)
        coin = 1
        ans_img = Fraction(0)
        for i in range(len(img)):
            ans_img += Fraction(ALPHABET.index(img[i]), base_from ** coin)
            coin += 1
        return ans_real + ans_img.numerator / ans_img.denominator if ans_img.numerator > 0 else ans_real

    else:
        if base_from == 'fac':
            # перевод из факториальной системы счисления (число должно быть целым)
            coin = len(numb)
            ans = 0
            for i in range(len(numb)):
                ans += numb[i] * factorial(coin)
                coin += 1
            return ans
        elif base_from == 'fib':
            # перевод из фибоначчиевой системы счисления (число должно быть целым)
            coin = 0
            ans = 0
            for i in range(len(numb) - 1, -1, -1):
                ans += int(numb[i]) * FIB_ALPHABET[coin]
                coin += 1
            return ans


def convert_to_base(numb: float, base_to) -> str:
    if type(base_to) == int:  # целочисленное основание
        if type(numb) == int:
            # число на входе целое
            if base_to < 0:
                ans = ''
                while True:
                    if numb % base_to == 0:
                        ans += '0'
                        numb //= base_to
                    else:
                        ans += str(abs(base_to) + (numb % base_to))  # из-за особенностей операнда % в python
                        numb //= base_to
                        numb += 1
                    if 1 <= numb <= 9:
                        ans += str(numb)
                        break
                return ans[::-1]
            else:
                ans = ''
                while numb > 0:
                    ans += ALPHABET[numb % base_to]
                    numb //= base_to
                return ans[::-1]
        else:
            # число на входе в формате десятичной дроби (основание должно быть положительным)
            real = int(str(numb)[:str(numb).index('.')])
            img = float('0' + str(numb)[str(numb).index('.'):])

            # переводим целую часть числа
            ans_real = ''
            while real > 0:
                ans_real += ALPHABET[real % base_to]
                real //= base_to
            ans_real = ans_real[::-1]

            # переводим дробную часть числа (до 6 знаков после запятой)
            ans_img = ''
            for i in range(7):
                ans_img += ALPHABET[int(img * base_to)]
                img = float('0' + str(img * base_to)[str(img * base_to).index('.'):])

            ans_img = ans_img.rstrip('0')  # избавляемся от лишних нулей с правой стороны
            return str(ans_real) + '.' + ans_img if len(ans_real) > 0 else '0.' + ans_img

    else:
        # фибоначчиева или факториальная система счисления (для данных систем счисления входное число должно быть целым и положительным)
        if base_to == 'fib':
            ans = ''
            for i in range(len(FIB_ALPHABET)):
                if FIB_ALPHABET[i] > numb:
                    for j in range(i - 1, -1, -1):
                        ans += str(numb // FIB_ALPHABET[j])
                        numb -= int(ans[-1]) * FIB_ALPHABET[j]
                    break
            return ans

        elif base_to == 'fac':
            ans = ''
            coin = 2
            while numb > 0:
                ans += str(numb % coin)
                numb //= coin
                coin += 1
            return ans[::-1]
