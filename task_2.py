from collections import Counter


QUERIS = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

total_count = len(QUERIS)
count_queries = Counter(QUERIS)
most_common_query, most_common_count = count_queries.most_common(1)[0]
share = most_common_count / total_count
single_queries = [
    query for query, count in count_queries.items() if count == 1
]

if __name__ == '__main__':
    print('Всего запросов:', total_count)
    print('Самый частый запрос:', most_common_query)
    print('Количество повторов самого частого запроса:', most_common_count)
    print('Доля самого частого запроса среди всех запросов:', share)
    print('Запросы, которые встречаются только один раз:', single_queries)
