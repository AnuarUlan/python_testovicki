import random
import re

class MathBot:
    def __init__(self):
        self.operations = ['+', '-', '*']

    def generate_problem(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(self.operations)
        problem = f"{a} {op} {b}"
        return problem

    def solve_problem(self, problem):
        try:
            # Простая защита: только цифры и операции
            if not re.match(r'^[0-9+\-*/ ().]+$', problem):
                return "Ошибка: недопустимые символы"
            result = eval(problem)
            return result
        except Exception as e:
            return f"Ошибка: {e}"


def main():
    bot = MathBot()

    print("Математический бот")
    print("1 - Сгенерировать задачу")
    print("2 - Решить задачу")
    print("0 - Выход")

    while True:
        choice = input("Выбери действие: ")

        if choice == '1':
            problem = bot.generate_problem()
            print(f"Задача: {problem}")
            answer = input("Твой ответ: ")
            correct = bot.solve_problem(problem)
            print(f"Правильный ответ: {correct}")

        elif choice == '2':
            problem = input("Введи задачу (например 2+2*3): ")
            result = bot.solve_problem(problem)
            print(f"Ответ: {result}")

        elif choice == '0':
            print("Пока!")
            break

        else:
            print("Неверный выбор")


if __name__ == '__main__':
    main()
