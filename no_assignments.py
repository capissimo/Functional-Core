# Эта программа получает три оценки за контрольные работы и
# показывает их средний балл. Она поздравляет пользователя, 
# если средний балл высокий.

def get_int(msg=''):
    return int(input(msg))

def printer(msg=''):
    def printfn(data):
        print(msg, data)
        return data
    return printfn    

def mapper(fn):
    return lambda seq: map(fn, seq)

def pipe(data, *fseq):
    for f in fseq:
        data = f(data)
    return data

# Именованная константа HIGH_SCORE содержит значение, которое
# считается высоким баллом.
def average_score(HIGH_SCORE):
    # Рассчитать средний балл.
    def average(seq):
        return sum(seq) / len(seq)
  
    # Если балл высокий, то поздравить пользователя.
    def test_score(average):
        if average >= HIGH_SCORE:
            print('Поздравляем!')
            print('Отличный средний балл!')
    
    pipe(['Введите оценку 1: ', 'Введите оценку 2: ', 'Введите оценку 3: '], # [str,str,str]
         mapper(get_int),                       # Получить три оценки.         # [int,int,int]
         list,
         average,                             # Усреднить оценки             # int
         printer('Средний балл составляет:'),  # Напечатать средний балл      # int
         test_score)                          # Проверить и поздравить       # -

# Вызвать главную функцию.
# Аргумент содержит значение, которое считается высоким баллом.
average_score(95) 
