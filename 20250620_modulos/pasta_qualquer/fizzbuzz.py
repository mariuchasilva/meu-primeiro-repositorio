def fizz_buzz(lista):
    for item in lista:
        if item % 3 == 0 and item % 5 == 0:
            print('fizzbuzz')
        elif item % 3 == 0:
            print('fizz')
        elif item % 5 == 0:
            print('buzz')