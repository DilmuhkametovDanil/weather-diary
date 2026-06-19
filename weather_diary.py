import json
import os
from datetime import datetime, timedelta

FILE_NAME = 'weather.json'


def load_data():
    """Загружает данные из JSON-файла."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_data(data):
    """Сохраняет данные в JSON-файл."""
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_record():
    """Добавляет запись за сегодня с указанием температуры и описания."""
    try:
        temperature = float(input("Введите температуру: "))
    except ValueError:
        print("Ошибка: температура должна быть числом!")
        return

    description = input("Введите описание погоды: ")

    record = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "temperature": temperature,
        "description": description
    }

    data = load_data()
    data.append(record)
    save_data(data)
    print("Запись добавлена!")


def show_all():
    """Выводит все записи."""
    data = load_data()
    print("\n=== Все записи ===")
    if not data:
        print("Записей нет.")
    else:
        for record in data:
            print(f"{record['date']} | {record['temperature']}°C | {record['description']}")


def show_last_week():
    """Выводит записи за последние 7 дней."""
    data = load_data()
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)

    print("\n=== Записи за неделю ===")
    found = False
    for record in data:
        record_date = datetime.strptime(record['date'], "%Y-%m-%d").date()
        if week_ago <= record_date <= today:
            print(f"{record['date']} | {record['temperature']}°C | {record['description']}")
            found = True

    if not found:
        print("Записей за последние 7 дней нет.")


def show_menu():
    """Показывает меню и обрабатывает выбор пользователя."""
    while True:
        print("\n=== Дневник погоды ===")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Показать записи за неделю")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_record()
        elif choice == '2':
            show_all()
        elif choice == '3':
            show_last_week()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")


if __name__ == '__main__':
    show_menu()
