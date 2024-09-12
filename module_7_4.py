def num(team1_num, team2_num):
    print('В команде %s участников: %s !' % (team1_num, team1_num))
    print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))


# Использование format:


def time(team1, score2, team1_time):
    print('Команда {} решила задач: {}!'.format(team1, score2))
    print('{} решили задачи за {} cек. !'.format(team1, team1_time))


# Использование f-строк:

def challenge_result(tasks_total, time_avg):
    print(f'Команды решили {score1} и {score2} задач')
    if score1 > score2:
        print(f'Результат битвы: победа команды {team1} !')
    else:
        print(f'Результат битвы: победа команды {team2} !')

    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')


score1 = 40
score2 = 42
team1 = 'Волшебники данных'
team2 = 'Мастера кода'
time_avg = 45.2
team1_time = 18015.2
team1_num = 6
team2_num = 7
tasks_total = 82
num(team1_num, team2_num)
time(team1, score2, team1_time)
challenge_result(tasks_total, time_avg)
