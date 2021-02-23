def game(number):
    Ones = number // 10
    Decimal = number % 10
    if Ones > Decimal or Ones ==Decimal:
        result = Ones - Decimal
    else:
        result = Decimal - Ones
    return result


print(game(92))