try:
    print( 100 / 0)
except ZeroDivisionError:
    print('Делить на ноль низя :С')
finally:
    print('Поэтому в игру вступает finally!')