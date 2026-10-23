import csv
import sys

INPUT_FILE = 'Corp_Summary.csv'
OUTPUT_FILE = 'departments_summary.csv'


def read_employees(filename=INPUT_FILE):
    employees = []
    with open(filename, 'r', encoding='utf-8', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)
        for row in reader:
            if not row:
                continue
            employees.append({
                'name': row[0],
                'department': row[1],
                'team': row[2],
                'position': row[3],
                'rating': float(row[4]),
                'salary': int(row[5]),
            })
    return employees


def build_hierarchy(employees):
    teams_by_department = {}
    for employee in employees:
        department = employee['department']
        team = employee['team']
        if department not in teams_by_department:
            teams_by_department[department] = []
        if team not in teams_by_department[department]:
            teams_by_department[department].append(team)

    for teams in teams_by_department.values():
        teams.sort()
    return teams_by_department


def build_summary(employees):
    salaries_by_department = {}
    for employee in employees:
        department = employee['department']
        if department not in salaries_by_department:
            salaries_by_department[department] = []
        salaries_by_department[department].append(employee['salary'])

    summary = []
    for department in sorted(salaries_by_department):
        salaries = salaries_by_department[department]
        summary.append([
            department,
            len(salaries),
            min(salaries),
            max(salaries),
            round(sum(salaries) / len(salaries), 2),
        ])
    return summary


def report_hierarchy(employees):
    hierarchy = build_hierarchy(employees)
    for department in sorted(hierarchy):
        print(department)
        for team in hierarchy[department]:
            print(f'  - {team}')


def report_summary(employees):
    summary = build_summary(employees)
    print(f'{"Департамент":<15}{"Сотрудников":>12}{"Мин":>10}'
          f'{"Макс":>10}{"Средняя":>12}')
    for department, count, min_salary, max_salary, avg_salary in summary:
        print(f'{department:<15}{count:>12}{min_salary:>10}'
              f'{max_salary:>10}{avg_salary:>12.2f}')


def report_summary_csv(employees, output_file=OUTPUT_FILE):
    summary = build_summary(employees)
    with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['Департамент', 'Сотрудников', 'Мин. оклад',
                         'Макс. оклад', 'Средний оклад'])
        writer.writerows(summary)
    print(f'Сводка записана в файл {output_file}')


def main(variant, output_file=OUTPUT_FILE):
    employees = read_employees()
    if variant == 1:
        report_hierarchy(employees)
    elif variant == 2:
        report_summary(employees)
    elif variant == 3:
        report_summary_csv(employees, output_file)
    else:
        print('Неизвестный вариант, выберите 1, 2 или 3')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Использование: python report.py <1|2|3>')
    else:
        main(int(sys.argv[1]))
