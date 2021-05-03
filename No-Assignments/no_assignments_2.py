# Программа без присаиваний

def get_int(msg=''):
    return int(input(msg))

def printer(*arg):
    def f(data):
        print(*arg, data, end=' ')
        return data
    return f

def reduce(function, seq, initializer=None):
    it = iter(seq)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = function(value, element)
    return value

def pipe(data, *fseq):
    for f in fseq: data = f(data)
    return data
    
def factorial():
    def error_handling(n):         # Обработка ошибок
        if not isinstance(n, int):
            raise TypeError("Число должно быть целым.")
        if not n >= 0:
            raise ValueError("Число должно быть ноль положительное.")
        return n

    #def factfn(number, acc=1):
    #    if number == 0: return acc
    #    return factfn(number - 1, acc * number)   # хвостовая рекурсия
    
    def factfn(n):
        return reduce(lambda x, y: x * y, range(1, n + 1)) # operator.mul
    
    pipe(get_int('Введите неотрицательное целое число: '), # int
         error_handling,                                   # int
         printer('Факториал числа'),                       # int
         factfn,                                           # int
         printer('равняется')                              # int
        )
    
# Вызвать главную функцию
factorial()
