import random
import json
import os

# -------------------------------
# Таблица рекордов
# -------------------------------
SCORE_FILE = "scores.json"

def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_score(name, score):
    scores = load_scores()
    scores[name] = max(score, scores.get(name, 0))
    
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f)

def show_scores():
    print("\n🏆 Таблица рекордов:")
    scores = load_scores()
    
    if not scores:
        print("Пока пусто!")
        return
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    for name, score in sorted_scores:
        print(f"{name}: {score}")

# -------------------------------
# 1. Викторина
# -------------------------------
def quiz():
    print("\n❓ Викторина")
    
    questions = [
        ("Столица Франции?", "париж"),
        ("2 + 2 * 2 = ?", "6"),
        ("Самая большая планета?", "юпитер")
    ]
    
    score = 0
    
    for q, a in questions:
        user = input(q + " ").lower()
        if user == a:
            print("Верно ✅")
            score += 1
        else:
            print("Неверно ❌")
    
    print(f"Ваш результат: {score}")
    name = input("Введите имя: ")
    save_score(name, score)

# -------------------------------
# 2. Угадай число
# -------------------------------
def guess_number():
    print("\n🔢 Угадай число (1-100)")
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Ваш вариант: "))
            attempts += 1
            
            if guess < number:
                print("Больше ⬆️")
            elif guess > number:
                print("Меньше ⬇️")
            else:
                print(f"Угадал за {attempts} попыток 🎉")
                name = input("Введите имя: ")
                save_score(name, max(0, 100 - attempts))
                break
        except:
            print("Введите число!")

# -------------------------------
# 3. Мини-RPG
# -------------------------------
def mini_rpg():
    print("\n⚔️ Мини-RPG")
    
    player_hp = 20
    enemy_hp = 15
    
    while player_hp > 0 and enemy_hp > 0:
        print(f"\nВаше HP: {player_hp} | Враг HP: {enemy_hp}")
        action = input("Атаковать (a) или лечиться (h): ")
        
        if action == "a":
            damage = random.randint(3, 7)
            enemy_hp -= damage
            print(f"Вы нанесли {damage} урона!")
        elif action == "h":
            heal = random.randint(2, 5)
            player_hp += heal
            print(f"Вы восстановили {heal} HP!")
        
        if enemy_hp > 0:
            enemy_damage = random.randint(2, 6)
            player_hp -= enemy_damage
            print(f"Враг атакует на {enemy_damage}")
    
    if player_hp > 0:
        print("Вы победили 🏆")
        name = input("Введите имя: ")
        save_score(name, 50)
    else:
        print("Вы проиграли 💀")

# -------------------------------
# Главное меню
# -------------------------------
def main():
    while True:
        print("\n====== Игровой помощник ======")
        print("1. Викторина")
        print("2. Угадай число")
        print("3. Мини-RPG")
        print("4. Таблица рекордов")
        print("5. Выход")
        
        choice = input("Выберите: ")
        
        if choice == "1":
            quiz()
        elif choice == "2":
            guess_number()
        elif choice == "3":
            mini_rpg()
        elif choice == "4":
            show_scores()
        elif choice == "5":
            print("Пока!")
            break
        else:
            print("Ошибка выбора!")

if __name__ == "__main__":
    main()
