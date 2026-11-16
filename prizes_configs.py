"""конфиг и процессор для призов"""
from json_dict_processing import create_processor

CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], int),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus'],
}


def prize_processor():
    """процессор списка призов"""
    return create_processor(CONFIG_PRIZE, list_processor=True)


if __name__ == '__main__':
    result = prize_processor()([{'awardYear': '2001', 'prizeAmount': 5}])
    assert result[0]['award_year'] == 2001
    assert result[0]['prize_amount'] == 5
    assert result[0]['category_en'] is None
    print('ok')
