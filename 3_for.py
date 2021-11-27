"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sales_info = [
    {'product': 'iPhone 12', 'items_sold': [
        363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [
     317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [
     343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main(items_qty):
    phone_qty = 0
    for qty in items_qty:
        phone_qty += qty
    return phone_qty


len_qty = 0
all_sum = 0
for product in sales_info:
    product_qty = main(product['items_sold'])
    product_qty_avg = round(
        main(product['items_sold'])/len(product['items_sold']), 1)
    all_sum += product_qty
    len_qty += len(product['items_sold'])
    print(f'Количество продаж {product["product"]} {product_qty}')
    print(f'Среднее количество продаж {product["product"]} {product_qty_avg}')
print(f'Суммарное кол-во продаж: {all_sum}')
print(f'Среднее кол-во продаж всех товаров: {all_sum/len_qty}')
