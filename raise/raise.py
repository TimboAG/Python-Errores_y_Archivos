def divir(a, b):
    if b == 0:
        raise ZeroDivisionError('Error: No se Puede divir por cero!')
    else:
        return a / b

divir(4, 0)