"""добавление и удаление полей в списке словарей (без изменения исходного)"""


def add_attribute(records, attribute, compute):
    """добавляет поле attribute = compute(запись) каждой записи"""
    return [{**record, attribute: compute(record)} for record in records]


def drop_attribute(records, attribute):
    """удаляет поле attribute у каждой записи"""
    return [{key: value for key, value in record.items() if key != attribute}
            for record in records]


if __name__ == '__main__':
    data = [{'a': 1, 'b': 2}]
    assert add_attribute(data, 'c', lambda row: row['a'] + row['b']) == [
        {'a': 1, 'b': 2, 'c': 3}]
    assert data == [{'a': 1, 'b': 2}]
    assert drop_attribute(data, 'b') == [{'a': 1}]
    print('ok')
