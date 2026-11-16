"""агрегации над списком плоских словарей"""
import statistics


def get_values(records, field):
    """значения поля без пропусков"""
    return [record[field] for record in records
            if record.get(field) is not None]


def count(records):
    """количество записей"""
    return len(records)


def mean(records, field):
    """среднее значение поля"""
    values = get_values(records, field)
    return statistics.mean(values) if values else None


def median(records, field):
    """медиана поля"""
    values = get_values(records, field)
    return statistics.median(values) if values else None


def maximum(records, field):
    """максимум поля"""
    values = get_values(records, field)
    return max(values) if values else None


def minimum(records, field):
    """минимум поля"""
    values = get_values(records, field)
    return min(values) if values else None


def top_n(metrics, n=5):
    """топ-n пар (ключ, значение) из словаря метрик"""
    return sorted(metrics.items(), key=lambda pair: pair[1], reverse=True)[:n]


def count_missing(records):
    """пропуски по полям: {'поле': число_пропусков}"""
    fields = {field for record in records for field in record}
    return {field: sum(record.get(field) is None for record in records)
            for field in sorted(fields)}


if __name__ == '__main__':
    data = [{'age': 20}, {'age': 40}, {'age': None}, {'age': 90}]
    assert count(data) == 4
    assert mean(data, 'age') == 50 and median(data, 'age') == 40
    assert maximum(data, 'age') == 90 and minimum(data, 'age') == 20
    assert top_n({'a': 1, 'b': 3, 'c': 2}, 2) == [('b', 3), ('c', 2)]
    assert count_missing(data) == {'age': 1}
    print('ok')
