"""
! MIHAMATH !
МАТЕМАТИЧЕСКИЙ МОДУЛЬ ОТ АВТОРА МИХАСОФТ
HTTPS://MIHASOFT.GLITCH.ME
"""
from math import acos, degrees

GB = 'gb'
MB = 'mb'
KB = 'kb'
B = 'b'


class ToBitsError(Exception):
    pass


class TriangleError(Exception):
    pass


class QuadrilateralError(Exception):
    pass


def _help():
    print('''Модуль MIHAMATH: много математических функций.
Список функций:

1. to_bits(number, from_what) - возвращает значение в битах числа, введённого в гига-, мега-, кило-, байтах.
  number: число гига-, мега-, кило-, байт;
  from_what: GB, MB, KB, B (соответственно размерности введённого значения).

2. Triangle(first_side, second_side, third_side) - создаёт объект треугольника с введёнными длинами сторон.
Для получения подробностей используйте Triangle.help().
''')


def to_bits(number, from_what):
    if from_what == GB or 'gb':
        return number * 1024 * 1024 * 1024 * 8
    elif from_what == MB or 'mb':
        return number * 1024 * 1024 * 8
    elif from_what == KB or 'kb':
        return number * 1024 * 8
    elif from_what == B or 'b':
        return number * 8
    else:
        raise ToBitsError(
            'Введён некорректный тип исходных данных: ' + from_what + '\n(используйте gb, mb, kb или b)')


class Triangle:

    def __init__(self, first_side: int, second_side: int, third_side: int):
        if first_side + second_side <= third_side or first_side + third_side <= second_side or \
                first_side + third_side <= second_side:
            raise TriangleError('Объект не является треугольником.')
        else:
            self.fs = first_side
            self.ss = second_side
            self.ts = third_side

    def __str__(self):
        return 'Треугольник: (' + str(self.fs) + ', ' + str(self.ss) + ', ' + str(self.ts) + ');'

    def is_equilateral(self):
        if self.fs == self.ss == self.ts:
            return True
        else:
            return False

    def is_isosceles(self):
        if self.fs == self.ss or self.fs == self.ts or self.ss == self.ts:
            return True
        else:
            return False

    def square(self):
        per = (self.fs + self.ss + self.ts) / 2
        return (per * (per - self.fs) * (per - self.ss) * (per - self.ts)) ** 0.5

    def create_similar_triangle(self, ratio: int):
        return Triangle(self.fs * ratio, self.ss * ratio, self.ts * ratio)

    def perimeter(self):
        return self.fs + self.ss + self.ts

    def height(self, side: int):
        if side == 1:
            return 2 * self.square() / self.fs
        elif side == 2:
            return 2 * self.square() / self.ss
        if side == 3:
            return 2 * self.square() / self.ts
        else:
            raise TriangleError('Неверный номер стороны: ' + str(side)
                                + '; Используйте 1, 2, 3.')

    def change(self, first_side: int, second_side: int, third_side: int):
        self.fs = first_side
        self.ss = second_side
        self.ts = third_side

    def angle(self, side: int):
        if side == 1:
            return int(degrees(acos((self.ts ** 2 + self.ss ** 2 - self.fs ** 2) / (2 * self.ts * self.ss))))

        elif side == 2:
            return int(degrees(acos((self.ts ** 2 + self.fs ** 2 - self.ss ** 2) / (2 * self.ts * self.fs))))

        elif side == 3:
            return int(degrees(acos((self.ss ** 2 + self.fs ** 2 - self.ts ** 2) / (2 * self.ss * self.fs))))

    def all_info(self):
        print('''
  ст. 1 = {}
          \   высота 1 = {}
           \     \     ^    высота 2 = {}
            \     \  /.3.\  /    
             \     \/..*..\/
              \    /.*.*.*.\  
               \  /....*....\  ст. 2 = {}
                \/..*..*..*..\    
                /2*....*....*1\\
               ========*========  <= Mст. 3 = {}
                      /    
         высота 3 = {}      

   '''.format(str(self.fs), str(self.height(1)), str(self.height(2)), str(self.ss), str(self.ts), str(self.height(3))))

        print('Треугольник (' + str(self.fs) + ', ' + str(self.ss) + ', ' + str(self.ts) + '):\n Периметр: ' + \
              str(self.perimeter()) + ';\n Площадь: ' + str(self.square()) + ';\n Высоты: ' + str(self.height(1)) + \
              ', ' + str(self.height(2)) + ', #' + str(self.height(3)) + ';\n Углы: 1: ' + str(self.angle(1)) + \
              ', 2: ' + str(self.angle(2)) + ', 3: ' + str(self.angle(3)) + '.')

    @staticmethod
    def help():
        print('''Используйте следующие методы для работы с треугольником:

is_equilateral() :
возвращает True, если треугольник равносторонний, иначе False.

is_isosceles() :
возвращает True, если треугольник равнобедренный, иначе False.

square() :
возвращает площадь треугольника.

perimeter() :
возвращает периметр треугольника.

create_similar_triangle(ratio) :
возвращает объект подобного данному треугольника с коэффициентом подобия ratio.

height(side) :
возвращает длину высоты, опущенной на сторону с номером side. Номера сторон в порядке ввода при создании треугольника.

change(first_side, second_side, third_side) :
переопределяет стороны треугольника на новые размеры.

all_info() :
печатает структурированно все данные о треугольнике.''')


class Quadrilateral:
    def __init__(self, first_side: int, second_side: int, third_side: int, fourth_side: int, _type='ordinary'):
        if _type != 'ordinary' and _type != 'parallelogram' and _type != 'square' and _type != 'trapezoid':
            raise QuadrilateralError('Введён некорректный тип четырёхугольника: {}.'.format(_type))
        elif _type == 'parallelogram' and (first_side != third_side) and (second_side != fourth_side):
            raise QuadrilateralError('Создаваемый четырёхугольник не является параллелограммом.')
        elif _type == 'square' and not (first_side == third_side == fourth_side == second_side):
            raise QuadrilateralError('Создаваемый четырёхугольник не является квадратом.')
        else:
            self.fs = first_side
            self.ss = second_side
            self.ts = third_side
            self.fos = fourth_side
            self.type = _type

    def __str__(self):
        return 'Четырёхугольник: ({}, {}, {}, {})'.format(self.fs, self.ss, self.ts, self.fos)

    def is_parallelogram(self):
        if (self.fs == self.ts) and (self.ss == self.fos):
            return True
        else:
            return False

    def perimeter(self):
        return self.fs + self.ss + self.ts + self.fos

    def square(self):
        if (self.fs != self.ss) and (self.fs != self.ts) and (self.fs != self.fos) and (self.ss != self.ts) and (
                self.ss != self.fos) and (self.ts != self.fos):
            raise QuadrilateralError('Операция не поддерживается для данного типа четырёхугольника')


if __name__ == '__main__':
    t = Triangle(10, 10, 10)
    t.all_info()
