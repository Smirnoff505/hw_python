from itertools import count


def total_revenue(purchases):
    """
     Рассчитайте и верните общую выручку (цена * количество для всех записей).
    """
    result = 0
    for purchase in purchases:
        item = purchase['price'] * purchase['quantity']
        result += item
    return result


def items_by_category(purchases):
    """
     Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
    """
    my_dict = {}

    for purchase in purchases:
        if purchase['category'] == 'fruit':
            my_dict.setdefault('fruit' , []).append(purchase['item'])
        elif purchase['category'] == 'dairy':
            my_dict.setdefault('dairy', []).append(purchase['item'])
        else:
            my_dict.setdefault('bread', []).append(purchase['item'])
    return my_dict


def expensive_purchases(purchases, min_price):
    """
     Выведите все покупки, где цена товара больше или равна min_price.
    """
    list_q = []
    for purchase in purchases:
        if purchase['price'] >= min_price:
            list_q.append(purchase)
        else:
            continue
    return list_q

def average_price_by_category(purchases):
    """
     Рассчитайте среднюю цену товаров по каждой категории.
    """
    total = {}
    count = {}

    for purchase in purchases:
        cat = purchase['category']
        qty = purchase['quantity']
        price = purchase['price']

        total[cat] = total.get(cat, 0) + qty * price
        count[cat] = count.get(cat, 0) + qty

    avg_price = {cat: round(total[cat] / count[cat], 2) for cat in total}
    return avg_price



def most_frequent_category(purchases):
    """
     Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).
    """
    my_dict = {}

    for purchase in purchases:
        my_dict.setdefault(purchase['category'],  0)
        item = purchase['category']
        my_dict[item] += purchase['quantity']

    category = max(my_dict, key=my_dict.get)
    return category
