"""конфиги и процессоры для лауреатов людей и организаций"""
from json_dict_processing import create_processor
from prizes_configs import prize_processor


def process_year(year_string):
    """год из 'YYYY-MM-DD' (бывают и неполные даты по типу '1917-00-00')"""
    year = year_string.split('-')[0]
    return int(year) if year.isdigit() else None


CONFIG_PERSON = {
    'id': (['id'], int),
    'name': (['knownName', 'en'], str.strip),
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor()),
}

CONFIG_ORG = {
    'id': (['id'], int),
    'name': (['orgName', 'en'], str.strip),
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor()),
}


def person_processor():
    """процессор лауреата человека"""
    return create_processor(CONFIG_PERSON)


def org_processor():
    """процессор лауреата-организации"""
    return create_processor(CONFIG_ORG)


process_persons = person_processor()
process_orgs = org_processor()


if __name__ == '__main__':
    assert process_year('1943-11-07') == 1943
    assert process_year('1917-00-00') == 1917
    person = process_persons({'id': '1', 'knownName': {'en': 'X '},
                              'nobelPrizes': [{'awardYear': '1950'}]})
    assert person['id'] == 1 and person['name'] == 'X'
    assert person['birth_year'] is None
    assert person['prizes_relevant'][0]['award_year'] == 1950
    print('ok')
