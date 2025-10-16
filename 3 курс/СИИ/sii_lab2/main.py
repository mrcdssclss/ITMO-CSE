from pyswip import Prolog
import re

prolog = Prolog()
prolog.consult("sii_lab1_shmidt.pl")

people = sorted([str(r["Person"]) for r in prolog.query("born(Person, _)")])


def normalize_name(name):
    name = name.strip().lower()
    name = re.sub(r'[^a-z0-9]', '_', name)
    name = re.sub(r'_+', '_', name)
    return name.strip('_')

def get_int(prompt):
    value = input(prompt)
    while not value.isdigit():
        print("Введите целое число.")
        value = input(prompt)
    return int(value)

def choose_person(prompt, people):
    print("\nСписок людей:")
    for i, p in enumerate(people, 1):
        print(f"{i}. {p}")
    value = input(prompt + " (имя или номер): ").strip()

    if value.isdigit():
        index = int(value)
        if 1 <= index <= len(people):
            return people[index - 1]
        else:
            print("Нет такого номера.")
            return choose_person(prompt, people)
    else:
        name = normalize_name(value)
        if name in people:
            return name
        print("Имя не найдено, попробуйте снова.")
        return choose_person(prompt, people)


def age_diff(p1, p2):
    res = list(prolog.query(f"age_diff({p1}, {p2}, Diff)"))
    return res[0]["Diff"] if res else None

def check_alive():
    person = choose_person("Введите имя человека", people)
    year = get_int("Введите год: ")
    result = list(prolog.query(f"alive({person}, {year})"))
    if result:
        print(f"{person} был(а) жив(а) в {year}.")
    else:
        print(f"{person} не был(а) жив(а) в {year}.")

def check_age():
    person = choose_person("Введите имя человека", people)
    year = get_int("Введите год: ")
    result = list(prolog.query(f"age({person}, {year}, Age)"))
    if result:
        print(f"Возраст {person} в {year}: {result[0]['Age']} лет.")
    else:
        print("Возраст не удалось определить.")

def check_marriage():
    p1 = choose_person("Первый человек", people)
    p2 = choose_person("Второй человек", people)
    year = get_int("Введите год: ")
    result = (list(prolog.query(f"are_married({p1}, {p2}, {year})")) or
              list(prolog.query(f"are_married({p2}, {p1}, {year})")))
    if result:
        print(f"{p1} и {p2} были женаты в {year}.")
    else:
        print(f"{p1} и {p2} не были женаты в {year}.")

def check_divorce():
    p1 = choose_person("Первый человек", people)
    p2 = choose_person("Второй человек", people)
    year = get_int("Введите год: ")
    result = (list(prolog.query(f"are_divorced({p1}, {p2}, {year})")) or
              list(prolog.query(f"are_divorced({p2}, {p1}, {year})")))
    if result:
        print(f"{p1} и {p2} были разведены в {year}.")
    else:
        print(f"{p1} и {p2} не были разведены в {year}.")

def check_older():
    p1 = choose_person("Первый человек", people)
    p2 = choose_person("Второй человек", people)
    result = list(prolog.query(f"older({p1}, {p2})"))
    if result:
        print(f"{p1} старше, чем {p2}.")
    else:
        print(f"{p1} не старше {p2}.")

def check_younger():
    p1 = choose_person("Первый человек", people)
    p2 = choose_person("Второй человек", people)
    result = list(prolog.query(f"younger({p1}, {p2})"))
    if result:
        print(f"{p1} младше, чем {p2}.")
    else:
        print(f"{p1} не младше {p2}.")

def check_same_age():
    p1 = choose_person("Первый человек", people)
    p2 = choose_person("Второй человек", people)
    result = list(prolog.query(f"same_age({p1}, {p2})"))
    if result:
        print(f"{p1} и {p2} одного возраста.")
    else:
        print(f"{p1} и {p2} родились в разные годы.")

def check_age_diff():
    p1 = choose_person("Первый человек", people)
    p2 = choose_person("Второй человек", people)
    diff = age_diff(p1, p2)
    if diff is not None:
        print(f"Разница в возрасте между {p1} и {p2}: {diff} лет.")
    else:
        print("Разница не определена.")

def check_parent():
    p1 = choose_person("Потенциальный родитель", people)
    p2 = choose_person("Потенциальный ребёнок", people)
    result = list(prolog.query(f"can_be_parent({p1}, {p2})"))
    if result:
        print(f"{p1} может быть родителем {p2}.")
    else:
        print(f"{p1} не может быть родителем {p2}.")

def check_child():
    person = choose_person("Введите имя", people)
    year = get_int("Введите год: ")
    result = list(prolog.query(f"child({person}, {year})"))
    if result:
        print(f"{person} считается ребёнком в {year}.")
    else:
        print(f"{person} не является ребёнком в {year}.")

def show_people():
    print("\nВсе люди в базе данных:")
    for p in people:
        print(" -", p)

def menu():
    print("""
1 — проверить жив ли человек
2 — найти возраст человека в заданном году
3 — проверить женаты ли люди в определенном году
4 — проверить разведены ли люди в заданном году
5 — найти кто из двух людей старше
6 — найти кто из двух людей младше
7 — найти одного ли года люди
8 — найти разницу в возресте среди двух людей
9 — проверить может ли один человек быть родителем для другого
10 — проверить является ли человек несовершеннолетним
0 — Выйти
""")

def main():
    print("Программа запущена.")
    print(f"Найдено людей: {len(people)}")

    while True:
        menu()
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            check_alive()
        elif choice == "2":
            check_age()
        elif choice == "3":
            check_marriage()
        elif choice == "4":
            check_divorce()
        elif choice == "5":
            check_older()
        elif choice == "6":
            check_younger()
        elif choice == "7":
            check_same_age()
        elif choice == "8":
            check_age_diff()
        elif choice == "9":
            check_parent()
        elif choice == "10":
            check_child()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Такого пункта нет. Попробуйте снова.")

main()