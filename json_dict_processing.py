"""превращение вложенного json-словаря в плоский по конфигу

формат конфига:
{'атрибут': ['путь', 'к', 'данным'],
 'атрибут_с_обработкой': (['путь', 'к', 'данным'], функция)}
"""


def extract_nested_value(obj, keys):
    """достаёт значение по цепочке ключей; если пути нет - возвращает None"""
    for key in keys:
        if not isinstance(obj, dict) or key not in obj:
            return None
        obj = obj[key]
    return obj


def process_dictionary_with_config(dictionary, config):
    """строит плоский словарь {атрибут: значение} по конфигу"""
    result = {}
    for attribute, rule in config.items():
        path, function = rule if isinstance(rule, tuple) else (rule, None)
        value = extract_nested_value(dictionary, path)
        if value is not None and function is not None:
            value = function(value)
        result[attribute] = value
    return result


def process_list_of_dicts_with_config(list_of_dicts, config):
    """применяет конфиг к каждому словарю из списка"""
    return [process_dictionary_with_config(item, config)
            for item in list_of_dicts or []]


def create_processor(config, list_processor=False):
    """возвращает функцию-обработчик с подставленным конфигом"""
    base_function = (process_list_of_dicts_with_config if list_processor
                     else process_dictionary_with_config)

    def processor(data):
        return base_function(data, config)

    return processor


if __name__ == '__main__':
    sample = {'id': '7', 'name': {'en': 'Alice'}}
    sample_config = {'id': (['id'], int), 'name': ['name', 'en'],
                     'age': ['age']}
    assert extract_nested_value(sample, ['name', 'en']) == 'Alice'
    assert extract_nested_value(sample, ['name', 'ru']) is None
    assert create_processor(sample_config)(sample) == {
        'id': 7, 'name': 'Alice', 'age': None}
    assert create_processor({'v': ['v']}, True)([{'v': 1}]) == [{'v': 1}]
    print('ok')
