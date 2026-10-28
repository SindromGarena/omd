REVIEWS = [
    {'id': 1, 'product': 'Чехол', 'stars': 5},
    {'id': 1, 'product': 'Чехол', 'stars': 3},
    {'id': 1, 'product': 'Чехол', 'stars': 4},
    {'id': 2, 'product': 'Наушники', 'stars': 2},
    {'id': 2, 'product': 'наушники', 'stars': 2},
    {'id': 2, 'product': 'НАУШНИКИ', 'stars': 5},
    {'id': 3, 'product': 'Планшет', 'stars': 5},
    {'id': 4, 'product': 'Колонка', 'stars': 4},
    {'id': 4, 'product': 'Колонка', 'stars': 4},
    {'id': 5, 'product': 'Кабель', 'stars': 1},
]

stars_by_product = {}
for review in REVIEWS:
    product = review['product'].capitalize()
    stars_by_product.setdefault(product, []).append(review['stars'])

average_stars = {
    product: sum(stars) / len(stars)
    for product, stars in stars_by_product.items()
}
rated_products = [
    product for product in average_stars
    if len(stars_by_product[product]) >= 2
]  # Просто ищем продукты с >=2 отзывами и берем минимум из них
worst_product = min(rated_products, key=average_stars.get)
low_star_count = sum(1 for review in REVIEWS if review['stars'] <= 2)
part_in_all = low_star_count / len(REVIEWS)


if __name__ == '__main__':
    print('Средняя оценка каждого товара:', average_stars)
    print('Худший товар среди тех, у кого от 2 отзывов:', worst_product)
    print('Отзывов на 1 или 2 звезды:', low_star_count)
    print('Их доля от всех отзывов:', part_in_all*100, '%')
