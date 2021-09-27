def get_vat(payment, percent=13):
    print(percent)
    try:
        payment = float(payment)
        print(payment)
        percent = int(percent)
        vat = payment / 100 * percent
        vat = round(vat,2)
        return 'Сумма НДФЛ: {}'.format(vat)
    except (TypeError, ValueError):
        print("не могу посчитать, проверьте вводимые данные")
result = get_vat(800, 15)
print(result)
