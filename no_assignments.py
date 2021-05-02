# Эта программа получает три оценки за контрольные работы и
# показывает их средний балл. Она поздравляет пользователя, 
# если средний балл высокий.

def get_int(msg=''):
    return int(input(msg))

def print_(msg=''):
    def printfn(data):
        print(msg, data)
        return data
    return printfn    

def map_(fn):
    return lambda seq: map(fn, seq)

def _(data, *fseq):
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
    
    _(['Введите оценку 1: ', 'Введите оценку 2: ', 'Введите оценку 3: '], # [str,str,str]
      map_(get_int),                       # Получить три оценки.         # [int,int,int]
      list,
      average,                             # Усреднить оценки             # int
      print_('Средний балл составляет:'),  # Напечатать средний балл      # int
      test_score)                          # Проверить и поздравить       # -

# Вызвать главную функцию.
# Аргумент содержит значение, которое считается высоким баллом.
average_score(95) 
