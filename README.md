# Учет финансов

Этот проект представляет собой приложение для управления финансами, реализованное на Python. Пользователь может вести учет своих финансов, записывая доходы и расходы, а также осуществлять поиск, редактирование и удаление транзакций.

## Использование

### Запуск приложения

Для запуска приложения выполните следующую команду в терминале:

После запуска приложения вы увидите меню с доступными действиями.

### Основные действия

1. **Вывести баланс** - отображает текущий баланс, а именно сумму всех доходов и расходов.

2. **Вывести доходы** - показывает список всех доходов, включая дату, категорию, сумму и описание.

3. **Вывести расходы** - показывает список всех расходов, включая дату, категорию, сумму и описание.

4. **Добавить транзакцию** - позволяет добавить новую транзакцию, указав дату, тип (доход или расход), сумму, категорию и описание.

5. **Поиск транзакций** - позволяет найти транзакции по различным критериям, таким как дата, сумма или категория.

6. **Редактировать транзакцию** - позволяет изменить существующую транзакцию, например, исправить ошибки или обновить данные.

7. **Удалить транзакцию** - позволяет удалить существующую транзакцию из списка.

8. **Выйти** - завершает работу приложения.

Выберите номер действия, введя соответствующую цифру, а затем следуйте инструкциям в консоли.

## Хранение данных

Все транзакции сохраняются в файле `transactions.csv`, который находится в папке `data` в корневой директории проекта. Этот файл содержит информацию о датах транзакций, их типе (доход или расход), сумме, категории и описании. При необходимости пользователь может редактировать этот файл напрямую или создать резервную копию данных.

## Автор

Автор: Vladimir Bryzgalov.
Контактная информация: vladimirbryzgalov00@gmail.com

