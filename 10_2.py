class MistypeError(Exception):
    def __init(self, text):
        self.text = text
try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print(a + b)
except ValueError:
    print('Ожидаемый тип данных - число')
