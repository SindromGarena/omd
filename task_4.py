DAYS = [
    {'day': 'пн', 'orders': 20, 'revenue': 40_000, 'returns': 2},
    {'day': 'вт', 'orders': 16, 'revenue': 19_200, 'returns': 4},
    {'day': 'ср', 'orders': 25, 'revenue': 55_000, 'returns': 1},
    {'day': 'чт', 'orders': 10, 'revenue': 12_000, 'returns': 3},
    {'day': 'пт', 'orders': 30, 'revenue': 48_000, 'returns': 3},
]


def get_revenue(day):
    return day['revenue']


week_revenue = sum(day['revenue'] for day in DAYS)
highest_revenue_day = max(DAYS, key=get_revenue)['day']
high_return_days = [
    day['day'] for day in DAYS
    if day['returns'] > day['orders'] * 0.2
]


if __name__ == '__main__':
    print('Выручка за неделю:', week_revenue)
    print('День с самой большой выручкой:', highest_revenue_day)
    print('Средняя выручка на один заказ по дням:')
    for day in DAYS:
        print(day['day'], day['revenue'] / day['orders'])
    print('Дни, где возвратов больше 20% заказов:', high_return_days)
