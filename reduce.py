
"""
Funkcja reduce() zwraca wynik redukcji, czyli pojedynczą wartość.
"""

#funkcja która przyjmuje dwa argumenty - dwa słowa 
# - i zwraca dłuższe z nich. W przypadku gdy słowa są tej samej długości funkcja zwróci drugi argument.

from functools import reduce
words = ['Python', 'jest', 'popularnym', 'językiem', 'programowania']

def longest_word(firstStr, secondStr):
    if len (firstStr) > len(secondStr):
        return firstStr
    elif len (firstStr) == len(secondStr):
        return secondStr
    else:
        return secondStr
    

theLongest = reduce(longest_word, words)
print(theLongest)

print('---')

# funkcja która przyjmuje słownik dotyczący 
# jednego zamówienia jako argument i oblicza 
# całkowity przychód z tego zamówienia, sumując ceny wszystkich pozycji w zamówieniu i dodając koszt wysyłki.
orders = [
    {
        'items': [
            ('Product 1', 10.99),
            ('Product 2', 20.99),
            ('Product 3', 5.99),
        ],
        'shipping': 5.0,
    },
    {
        'items': [
            ('Product 4', 15.99), 
            ('Product 5', 8.99)
        ],
        'shipping': 7.5,
    },
    {
        'items': [
            ('Product 6', 12.99),
            ('Product 7', 9.99),
            ('Product 8', 14.99),
        ],
        'shipping': 10.0,
    },
]



def order_revenue(yourOrders):
    order = list(map(lambda x: sum(item[1] for item in x['items']) + x['shipping'], yourOrders))
    return order

threeOrder = order_revenue(orders)

def sumTotal (x, y):
    return x + y

print(f"Total revenue: {reduce(sumTotal, threeOrder, 0)}")