from data_manager import DataManager
from function import *


def main():
    """
    Основная функция управления приложением.

    Функция запускает бесконечный цикл, в котором пользователь выбирает действие из списка:
    - Вывести баланс
    - Вывести доходы
    - Вывести расходы
    - Добавить транзакцию
    - Поиск транзакций
    - Редактировать транзакцию
    - Удалить транзакцию
    - Выйти из приложения
    """
    path_to_transaction_file = r'data\transactions.csv'
    data_manager = DataManager(path_to_transaction_file)

    while True:
        print(f"{'-'*20}\nВыберите действие:")
        print("1. Вывести баланс 💵")
        print("2. Вывести доходы 📈")
        print("3. Вывести расходы 📉")
        print("4. Добавить транзакцию ➕")
        print("5. Поиск транзакций 🔎")
        print("6. Редактировать транзакцию 📝")
        print("7. Удалить транзакцию 🗑️")
        print("8. Выйти 👋")

        choice = input(f"{'-'*20}\nВведите номер действия: ")

        if choice == "1":
            print_balance(data_manager)
        elif choice == "2":
            print_incomes(data_manager)
        elif choice == "3":
            print_expenses(data_manager)
        elif choice == "4":
            add_transaction(data_manager)
        elif choice == "5":
            search_transactions(data_manager)
        elif choice == "6":
            edit_transaction(data_manager)
        elif choice == "7":
            delete_transaction(data_manager)
        elif choice == "8":
            print("Завершение работы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
