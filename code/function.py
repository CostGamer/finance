from data_manager import DataManager
from datetime import datetime


def print_balance(data_manager: DataManager) -> None:
    """
    Выводит информацию о текущем балансе.

    Функция считывает данные о транзакциях с помощью объекта DataManager,
    затем вычисляет общий доход, общие расходы и текущий баланс. Информация
    выводится на экран в формате:

    Текущий баланс:
    Доходы: [сумма доходов]
    Расходы: [сумма расходов]
    Баланс: [текущий баланс]
    """
    transactions_data = data_manager.read_transactions()
    total_income = sum(float(transaction['Сумма'])
                       for transaction in transactions_data if transaction['Тип'] == 'доход')
    total_expenses = sum(float(
        transaction['Сумма']) for transaction in transactions_data if transaction['Тип'] == 'расход')
    total_balance = total_income - total_expenses

    print()
    print("Текущий баланс:")
    print(f"Доходы: {total_income}")
    print(f"Расходы: {total_expenses}")
    print(f"Баланс: {total_balance}")


def print_incomes(data_manager: DataManager) -> None:
    """
    Выводит информацию о доходах.

    Функция считывает данные о транзакциях с помощью объекта DataManager
    и выводит на экран информацию о транзакциях, у которых тип равен 'доход'.
    Для каждой транзакции выводится дата, категория (если указана), сумма и описание.
    """
    transactions_data = data_manager.read_transactions()
    print("\nДоходы:")
    for transaction in transactions_data:
        if transaction['Тип'] == 'доход':
            print(f"Дата: {transaction['Дата']}, Категория: {transaction['Категория']}, Сумма: {
                  transaction['Сумма']} рублей, Описание: {transaction['Описание']}")


def print_expenses(data_manager: DataManager) -> None:
    """
    Выводит информацию о расходах.

    Функция считывает данные о транзакциях с помощью объекта DataManager
    и выводит на экран информацию о транзакциях, у которых тип равен 'расход'.
    Для каждой транзакции выводится дата, категория (если указана), сумма и описание.
    """
    transactions_data = data_manager.read_transactions()
    print("\nРасходы:")
    for transaction in transactions_data:
        if transaction['Тип'] == 'расход':
            print(f"Дата: {transaction['Дата']}, Категория: {transaction['Категория']}, Сумма: {
                  transaction['Сумма']} рублей, Описание: {transaction['Описание']}")


def add_transaction(data_manager: DataManager) -> None:
    """
    Добавляет новую транзакцию.

    Функция запрашивает у пользователя информацию о новой транзакции, такую как
    дата, сумма, описание, тип (доход или расход) и категория.
    Проверяет корректность, введенных, данных.
    Если данные введены корректно, создает словарь с информацией о транзакции и добавляет его
    в список существующих транзакций. Затем записывает обновленные данные в файл.
    """
    while True:
        flag_data = False
        flag_amount = False
        flag_option = False

        while flag_data != True:
            # Проверяем правильность формата даты
            try:
                date_str = input("Введите дату транзакции (гггг-мм-дд): ")
                datetime.strptime(date_str, "%Y-%m-%d")
                flag_data = True
            except ValueError:
                print("Неверный формат даты. Повторите ввод.")

        while flag_amount != True:
            # Проверяем, что сумма может быть преобразована в число
            try:
                amount_str = input("Введите сумму транзакции: ")
                num = float(amount_str)
                if num > 0:
                    flag_amount = True
                else:
                    print('Сумма не может быть отрицательной')
            except ValueError:
                print("Сумма должна быть числом. Повторите ввод.")

        description = input("Введите описание транзакции: ")

        while flag_option != True:
            type_str = input("Введите тип транзакции (доход/расход): ").lower()
            # Проверяем, что тип транзакции указан корректно
            if type_str not in ['доход', 'расход']:
                print(
                    "Тип транзакции должен быть 'доход' или 'расход'. Повторите ввод.")
            else:
                flag_option = True

        category = input("Введите категорию транзакции: ").lower()

        # Создаем словарь для новой транзакции
        new_transaction: dict[str, str] = {'Дата': date_str, 'Тип': type_str,
                                           'Сумма': amount_str, 'Описание': description, 'Категория': category}

        # Добавляем новую транзакцию
        transactions_data = data_manager.read_transactions()
        transactions_data.append(new_transaction)
        data_manager.write_transactions(transactions_data)
        break


def search_transactions(data_manager: DataManager) -> None:
    """
    Позволяет пользователю выполнять поиск транзакций по различным критериям, таким как категория,
    сумма или дата.

    Функция запрашивает у пользователя способ поиска транзакций: по категории, сумме или дате.
    Затем запрашивает соответствующие данные для поиска и выводит найденные транзакции или сообщает,
    что транзакции не найдены.
    """
    flag_search = False

    print()
    while flag_search != True:
        search_by = input(
            "Выберите способ поиска (категория/сумма/дата): ").lower()
        # Проверяем, правильно ли введены данные
        if search_by not in ['категория', 'сумма', 'дата']:
            print(
                "Тип транзакции должен быть 'категория' или 'сумма' или 'дата'. Повторите ввод.")
        else:
            flag_search = True

    if search_by == "категория":
        category = input("Введите категорию для поиска: ")
        transactions_data = data_manager.read_transactions()
        found_transactions = [transaction for transaction in transactions_data if transaction.get(
            'Категория') == category]
        if found_transactions:
            print()
            print("Найденные транзакции:")
            for transaction in found_transactions:
                print(f"Дата: {transaction['Дата']}, Категория: {transaction['Категория']}, Сумма: {
                    transaction['Сумма']} рублей, Описание: {transaction['Описание']}")
        else:
            print()
            print("Транзакции с указанной категорией не найдены.")

    elif search_by == "сумма":
        while True:
            amount = input("Введите сумму для поиска: ")
            try:
                amount_float = float(amount)
                if amount_float >= 0:
                    break
                else:
                    print("Сумма не может быть отрицательной.")
            except ValueError:
                print("Сумма должна быть числом. Повторите ввод.")

        transactions_data = data_manager.read_transactions()
        found_transactions = [
            transaction for transaction in transactions_data if transaction.get('Сумма') == amount]
        if found_transactions:
            print()
            print("Найденные транзакции:")
            for transaction in found_transactions:
                print(f"Дата: {transaction['Дата']}, Категория: {transaction['Категория']}, Сумма: {
                    transaction['Сумма']} рублей, Описание: {transaction['Описание']}")
        else:
            print()
            print("Транзакции с указанной суммой не найдены.")

    elif search_by == "дата":
        while True:
            date = input("Введите дату для поиска (гггг-мм-дд): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Неверный формат даты. Повторите ввод.")

        transactions_data = data_manager.read_transactions()
        found_transactions = [
            transaction for transaction in transactions_data if transaction.get('Дата') == date]
        if found_transactions:
            print()
            print("Найденные транзакции:")
            for transaction in found_transactions:
                print(f"Дата: {transaction['Дата']}, Категория: {transaction['Категория']}, Сумма: {
                    transaction['Сумма']} рублей, Описание: {transaction['Описание']}")
        else:
            print()
            print("Транзакции с указанной датой не найдены.")


def edit_transaction(data_manager: DataManager) -> None:
    """
    Позволяет пользователю редактировать выбранную транзакцию.

    Функция выводит список всех транзакций и запрашивает у пользователя номер транзакции для редактирования.
    Затем пользователь выбирает поле для редактирования из предложенных опций и вводит новое значение для этого поля.
    Функция проверяет корректность введенных данных (даты, числа, типа транзакции) и обновляет соответствующее
    поле в выбранной транзакции. После успешного редактирования транзакции происходит сохранение изменений.
    """
    print()
    while True:
        transactions_data = data_manager.read_transactions()
        print("Список всех транзакций:")
        for i, transaction in enumerate(transactions_data):
            print(f"{i + 1}. {transaction}")
        print()

        while True:
            try:
                index = int(
                    input("Введите номер транзакции для редактирования (или 0 для отмены): "))
                if index == 0:
                    print("Отмена редактирования.")
                    return
                elif 0 < index <= len(transactions_data):
                    break
                else:
                    print("Неверный номер транзакции. Попробуйте снова.")
            except ValueError:
                print("Введите целое число.")

        transaction_to_edit = transactions_data[index - 1]
        print()
        print("Текущая транзакция для редактирования:")
        print(f"Дата: {transaction_to_edit['Дата']}, Категория: {transaction_to_edit.get('Категория', 'N/A')}, Сумма: {
            transaction_to_edit['Сумма']} рублей, Описание: {transaction_to_edit['Описание']}")
        print()

        # Получаем список полей для редактирования
        fields = ['Дата', 'Сумма', 'Описание', 'Тип', 'Категория']
        print("Выберите поле для редактирования:")
        for i, field in enumerate(fields, start=1):
            print(f"{i}. {field}")

        while True:
            try:
                choice = int(
                    input("Введите номер поля для редактирования (или 0 для отмены): "))
                if choice == 0:
                    print("Отмена редактирования.")
                    break
                elif 0 < choice <= len(fields):
                    field_to_edit = fields[choice - 1]
                    new_value = input(f"Введите новое значение для поля '{
                                      field_to_edit}': ")
                    # Обновляем значение поля в транзакции
                    if field_to_edit == 'Дата':
                        while True:
                            try:
                                datetime.strptime(new_value, "%Y-%m-%d")
                                break
                            except ValueError:
                                print("Неверный формат даты. Повторите ввод.")
                                new_value = input(f"Введите новое значение для поля '{
                                                  field_to_edit}': ")
                    elif field_to_edit == 'Сумма':
                        while True:
                            try:
                                num = float(new_value)
                                if num > 0:
                                    break
                                else:
                                    print("Сумма не может быть отрицательной")
                                    new_value = input(f"Введите новое значение для поля '{
                                                      field_to_edit}': ")
                            except ValueError:
                                print("Сумма должна быть числом. Повторите ввод.")
                                new_value = input(f"Введите новое значение для поля '{
                                                  field_to_edit}': ")
                    elif field_to_edit == 'Тип':
                        while True:
                            new_value = new_value.lower()
                            if new_value in ['доход', 'расход']:
                                break
                            else:
                                print(
                                    "Тип транзакции должен быть 'доход' или 'расход'. Повторите ввод.")
                                new_value = input(f"Введите новое значение для поля '{
                                                  field_to_edit}': ")
                    transaction_to_edit[field_to_edit] = new_value
                else:
                    print("Неверный номер поля. Попробуйте снова.")
            except ValueError:
                print("Введите целое число.")

        data_manager.write_transactions(transactions_data)
        print()
        print("Транзакция успешно отредактирована.")
        print()


def delete_transaction(data_manager: DataManager) -> None:
    """
    Позволяет пользователю удалить выбранную транзакцию.

    Функция выводит список всех транзакций и запрашивает у пользователя номер транзакции для удаления.
    После подтверждения удаления, функция удаляет выбранную транзакцию из списка и сохраняет обновленные данные.
    """
    print()
    while True:
        transactions_data = data_manager.read_transactions()
        print("Список всех транзакций:")
        for i, transaction in enumerate(transactions_data):
            print(f"{i + 1}. {transaction}")

        while True:
            try:
                print()
                index = int(
                    input("Введите номер транзакции для удаления (или 0 для отмены): "))
                if index == 0:
                    print("Отмена удаления.")
                    return
                elif 0 < index <= len(transactions_data):
                    break
                else:
                    print()
                    print("Неверный номер транзакции. Попробуйте снова.")
            except ValueError:
                print("Введите целое число.")

        del transactions_data[index - 1]

        data_manager.write_transactions(transactions_data)
        print("Транзакция успешно удалена.")
