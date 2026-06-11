import sys
from typing import List, Tuple
sys.set_int_max_str_digits(5000)

def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            # Примітка: додає цілий список, як у твоєму шаблоні
            temp.append(el_second_list)
    return temp


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int:
    while n > 1:
          n //= 2
    return n


if __name__ == '__main__':
    print("--- Тестування функцій ---")

    # Тест для списків однаковою довжиною N = 3
    list_a = [1, 2, 3]
    list_b = [2, 3, 4]

    print(f"Question 1: {question1(list_a, list_b)}")
    print(f"Question 2: {question2(1)}")
    print(f"Question 3: {question3(list_a, list_b)}")
    print(f"Question 4: {question4([1, 5, 3, 9, 2])}")
    print(f"Question 5: {question5(3)}")
    print(f"Question 6: {question6(16)}")