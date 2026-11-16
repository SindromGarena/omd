"""аналоги sql where и group by для списка плоских словарей"""


def filter_records(records, condition):
    """where: оставляет записи, для которых condition(запись) истинно"""
    return [record for record in records if condition(record)]


def group_by_attributes(records, attributes):
    """group by: {(значения полей attributes): [записи группы]}"""
    groups = {}
    for record in records:
        key = tuple(record.get(attribute) for attribute in attributes)
        groups.setdefault(key, []).append(record)
    return groups


def apply_aggregation(groups, aggregation, *args):
    """применяет aggregation(записи, *args) к каждой группе"""
    return {key: aggregation(records, *args)
            for key, records in groups.items()}


if __name__ == '__main__':
    data = [{'country': 'USA', 'age': 25}, {'country': 'UK', 'age': 30},
            {'country': 'USA', 'age': 25}]
    groups = group_by_attributes(data, ['country', 'age'])
    assert groups == {('USA', 25): [data[0], data[2]], ('UK', 30): [data[1]]}
    assert filter_records(data, lambda row: row['age'] > 26) == [data[1]]
    assert apply_aggregation(groups, len) == {('USA', 25): 2, ('UK', 30): 1}
    print('ok')
