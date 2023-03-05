"""Игра угадай число v3
Компьютер сам загадывает и сам угадывает число
Задача этой версии, улучшить алгоритм таким образом, чтобы число было угадано за 20 попыток или меньше
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число от 1 до 100, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Кол-во попыток
    predict = np.random.randint(1, 101) # Предполагаемое число
    predict_1 = 1 # Начальная точка интервала чисел
    predict_2 = 101 # Конечная точка интервала чисел
    
    while number != predict:
        count += 1
        if number > predict:
            predict_1 = predict # Новая начальная точка, которая подразумевает, что загаданное число больше предполагаемого
            predict = np.random.randint(predict_1, predict_2)
  
        elif number < predict:
            predict_2 = predict # Новая начальная точка, которая подразумевает, что загаданное число меньше предполагаемого
            predict = np.random.randint(predict_1, predict_2)
            
    return count # Возвращаем число попыток


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
print('Run benchmarking for game_core_v3: ', end='')


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)