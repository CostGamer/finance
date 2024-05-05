import csv
import os


class DataManager:
    def __init__(self, transactions_file: str):
        self.transactions_file = transactions_file
        self.create_file_if_not_exist()

    def create_file_if_not_exist(self) -> None:
        """
        Создает файл для хранения транзакций, если он не существует.

        Если файл с указанным именем не существует, функция создает новый файл
        и записывает заголовок (шапку) таблицы транзакций с заданными полями.
        Поля в заголовке включают дату, тип транзакции, сумму, категорию и описание.
        """
        if not os.path.exists(self.transactions_file):
            with open(self.transactions_file, 'w', newline='') as csvfile:
                fieldnames = ['Дата', 'Тип', 'Сумма', 'Категория', 'Описание']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

    def read_transactions(self) -> list[dict[str, str]]:
        """
        Читает данные о транзакциях из файла и возвращает их в виде списка словарей.

        Функция открывает файл с транзакциями для чтения и считывает содержимое.
        Данные о транзакциях представлены в формате CSV. Каждая транзакция
        представлена в виде словаря, где ключи - это названия полей транзакции,
        а значения - соответствующие значения полей.
        """
        transactions_data = []
        with open(self.transactions_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions_data.append(row)
        return transactions_data

    def write_transactions(self, transactions_data: list[dict[str, str]]) -> None:
        """
        Записывает данные о транзакциях в файл.

        Функция принимает список словарей, представляющих транзакции, и записывает
        их в файл в формате CSV. Каждая транзакция представлена в виде словаря,
        где ключи - это названия полей транзакции, а значения - соответствующие
        значения полей.
        """
        with open(self.transactions_file, 'w', newline='') as csvfile:
            fieldnames = ['Дата', 'Тип', 'Сумма', 'Категория', 'Описание']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in transactions_data:
                writer.writerow(transaction)
