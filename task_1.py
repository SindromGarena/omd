MOSCOW = {201, 202, 203, 204}
KAZAN = {203, 204, 205, 206}


any_city_ids = MOSCOW | KAZAN
only_moscow_ids = MOSCOW - KAZAN
only_kazan_ids = KAZAN - MOSCOW
total_count = len(any_city_ids)


if __name__ == '__main__':
    print('Можно забрать в любом городе:', any_city_ids)
    print('Есть только в Москве:', only_moscow_ids)
    print('Есть только в Казани:', only_kazan_ids)
    print('Всего разных товаров на обоих складах:', total_count)
