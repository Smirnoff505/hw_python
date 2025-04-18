from functions import total_revenue, items_by_category, expensive_purchases, most_frequent_category, \
    average_price_by_category

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(f'Общая выручка: {total_revenue(purchases)}\n'
            f'Товары по категориям: {items_by_category(purchases)}\n'
            f'Покупки дороже 1.0: {expensive_purchases(purchases, min_price=1.0)}\n'
            f'Средняя цена по категориям: {average_price_by_category(purchases)}\n'
            f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')

