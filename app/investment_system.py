import sqlite3
from datetime import datetime

DB_NAME = "investment_system.db"

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def execute_query(self, query, params=()):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()

    def fetchone(self, query, params=()):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        conn.close()
        return result

    def fetchall(self, query, params=()):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()
        return result

class Client:
    def __init__(self, client_id, name, ownership_type, address, phone):
        self.client_id = client_id
        self.name = name
        self.ownership_type = ownership_type
        self.address = address
        self.phone = phone

    def save(self, db):
        try:
            db.execute_query(
                '''INSERT INTO "Клиент" VALUES (?, ?, ?, ?, ?)''',
                (self.client_id, self.name, self.ownership_type, self.address, self.phone)
            )
            print("Клиент успешно добавлен.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def update(self, db):
        try:
            db.execute_query(
                '''UPDATE "Клиент" SET
                    "Название предприятия" = COALESCE(NULLIF(?, ''), "Название предприятия"),
                    "Вид собственности" = COALESCE(NULLIF(?, ''), "Вид собственности"),
                    "Адрес" = COALESCE(NULLIF(?, ''), "Адрес"),
                    "Телефон" = COALESCE(NULLIF(?, ''), "Телефон")
                WHERE "ID Клиента" = ?''',
                (self.name, self.ownership_type, self.address, self.phone, self.client_id)
            )
            print("Информация о клиенте обновлена.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def delete(self, db):
        try:
            db.execute_query('''DELETE FROM "Клиент" WHERE "ID Клиента" = ?''', (self.client_id,))
            print("Клиент удалён.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def get_report(self, db):
        try:
            client_data = db.fetchone('''SELECT * FROM "Клиент" WHERE "ID Клиента" = ?''', (self.client_id,))
            if client_data:
                print("\nИнформация о клиенте:")
                print(f"ID Клиента: {client_data[0]}")
                print(f"Название предприятия: {client_data[1]}")
                print(f"Вид собственности: {client_data[2]}")
                print(f"Адрес: {client_data[3]}")
                print(f"Телефон: {client_data[4]}")

                projects = db.fetchall('''SELECT * FROM "Инвестиционный проект" WHERE "ID Клиента" = ?''', (self.client_id,))
                if projects:
                    print("\nПроекты клиента:")
                    for project in projects:
                        print(f"\n  ID Проекта: {project[0]}")
                        print(f"  Название проекта: {project[1]}")
                        print(f"  Сумма инвестиций: {project[2]}")
                        print(f"  Дата начала: {project[3]}")
                        print(f"  Дата завершения: {project[4]}")

                else:
                    print("\nУ клиента нет проектов.")
            else:
                print("Клиент с указанным ID не найден.")
        except Exception as e:
            print(f"Ошибка: {e}")

class Project:
    def __init__(self, project_id, name, investment_amount, start_date, end_date, client_id):
        self.project_id = project_id
        self.name = name
        self.investment_amount = investment_amount
        self.start_date = start_date
        self.end_date = end_date
        self.client_id = client_id

    def save(self, db):
        try:
            db.execute_query(
                '''INSERT INTO "Инвестиционный проект" VALUES (?, ?, ?, ?, ?, ?)''',
                (self.project_id, self.name, self.investment_amount, self.start_date, self.end_date, self.client_id)
            )
            print("Проект успешно добавлен.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def update(self, db):
        try:
            db.execute_query(
                '''UPDATE "Инвестиционный проект" SET
                    "Название проекта" = COALESCE(NULLIF(?, ''), "Название проекта"),
                    "Сумма инвестиций" = COALESCE(NULLIF(?, ''), "Сумма инвестиций"),
                    "Дата начала" = COALESCE(NULLIF(?, ''), "Дата начала"),
                    "Дата завершения" = COALESCE(NULLIF(?, ''), "Дата завершения")
                WHERE "ID Проекта" = ?''',
                (self.name, self.investment_amount, self.start_date, self.end_date, self.project_id)
            )
            print("Информация о проекте обновлена.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def delete(self, db):
        try:
            db.execute_query('''DELETE FROM "Инвестиционный проект" WHERE "ID Проекта" = ?''', (self.project_id,))
            print("Проект удалён.")
        except Exception as e:
            print(f"Ошибка: {e}")

class Security:
    def __init__(self, security_id, security_type, issue_date, maturity_date, profitability):
        self.security_id = security_id
        self.security_type = security_type
        self.issue_date = issue_date
        self.maturity_date = maturity_date
        self.profitability = profitability

    def save(self, db):
        try:
            db.execute_query(
                '''INSERT INTO "Ценные бумаги" VALUES (?, ?, ?, ?, ?)''',
                (self.security_id, self.security_type, self.issue_date, self.maturity_date, self.profitability)
            )
            print("Ценная бумага успешно добавлена.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def update(self, db):
        try:
            db.execute_query(
                '''UPDATE "Ценные бумаги" SET
                    "Тип ценной бумаги" = COALESCE(NULLIF(?, ''), "Тип ценной бумаги"),
                    "Дата выпуска" = COALESCE(NULLIF(?, ''), "Дата выпуска"),
                    "Дата погашения" = COALESCE(NULLIF(?, ''), "Дата погашения"),
                    "Доходность" = COALESCE(NULLIF(?, ''), "Доходность")
                WHERE "ID Ценной бумаги" = ?''',
                (self.security_type, self.issue_date, self.maturity_date, self.profitability, self.security_id)
            )
            print("Ценная бумага обновлена.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def delete(self, db):
        try:
            db.execute_query('''DELETE FROM "Ценные бумаги" WHERE "ID Ценной бумаги" = ?''', (self.security_id,))
            print("Ценная бумага удалена.")
        except Exception as e:
            print(f"Ошибка: {e}")

class InvestmentSystem:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def initialize_database(self):
        try:
            self.db.execute_query('''CREATE TABLE IF NOT EXISTS "Клиент" (
                "ID Клиента" INTEGER PRIMARY KEY,
                "Название предприятия" TEXT,
                "Вид собственности" TEXT,
                "Адрес" TEXT,
                "Телефон" TEXT
            );''')

            self.db.execute_query('''CREATE TABLE IF NOT EXISTS "Инвестиционный проект" (
                "ID Проекта" INTEGER PRIMARY KEY,
                "Название проекта" TEXT,
                "Сумма инвестиций" REAL,
                "Дата начала" TEXT,
                "Дата завершения" TEXT,
                "ID Клиента" INTEGER,
                FOREIGN KEY ("ID Клиента") REFERENCES "Клиент"("ID Клиента")
            );''')

            self.db.execute_query('''CREATE TABLE IF NOT EXISTS "Ценные бумаги" (
                "ID Ценной бумаги" INTEGER PRIMARY KEY,
                "Тип ценной бумаги" TEXT,
                "Дата выпуска" TEXT,
                "Дата погашения" TEXT,
                "Доходность" REAL
            );''')

            self.db.execute_query('''CREATE TABLE IF NOT EXISTS "Сведения о проекте" (
                "ID Проекта" INTEGER,
                "ID Ценной бумаги" INTEGER,
                PRIMARY KEY ("ID Проекта", "ID Ценной бумаги"),
                FOREIGN KEY ("ID Проекта") REFERENCES "Инвестиционный проект"("ID Проекта"),
                FOREIGN KEY ("ID Ценной бумаги") REFERENCES "Ценные бумаги"("ID Ценной бумаги")
            );''')

            print("База данных и таблицы инициализированы.")
        except Exception as e:
            print(f"Ошибка при инициализации базы данных: {e}")

def main():
    system = InvestmentSystem(DB_NAME)
    system.initialize_database()

    while True:
        print("\nМеню:")
        print("1. Добавить клиента")
        print("2. Добавить проект")
        print("3. Добавить ценную бумагу")
        print("4. Обновить данные клиента")
        print("5. Обновить проект")
        print("6. Обновить ценную бумагу")
        print("7. Удалить клиента")
        print("8. Удалить проект")
        print("9. Удалить ценную бумагу")
        print("10. Сформировать отчет по клиенту")
        print("11. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            client = Client(int(input("Введите ID клиента: ")), input("Название: "), input("Вид собственности: "), input("Адрес: "), input("Телефон: "))
            client.save(system.db)
        elif choice == '2':
            project = Project(int(input("Введите ID проекта: ")), input("Название: "), float(input("Сумма: ")), input("Дата начала: "), input("Дата окончания: "), int(input("ID клиента: ")))
            project.save(system.db)
        elif choice == '3':
            security = Security(int(input("ID ценной бумаги: ")), input("Тип: "), input("Дата выпуска: "), input("Дата погашения: "), float(input("Доходность: ")))
            security.save(system.db)
        elif choice == '5':
            project_id = int(input("Введите ID проекта для обновления: "))
            project = Project(project_id, input("Название: "), float(input("Сумма: ")), input("Дата начала: "), input("Дата окончания: "), int(input("ID клиента: ")))
            project.update(system.db)
        elif choice == '6':
            security_id = int(input("Введите ID ценной бумаги для обновления: "))
            security = Security(security_id, input("Тип: "), input("Дата выпуска: "), input("Дата погашения: "), float(input("Доходность: ")))
            security.update(system.db)
        elif choice == '8':
            project_id = int(input("Введите ID проекта для удаления: "))
            project = Project(project_id, '', 0, '', '', 0)
            project.delete(system.db)
        elif choice == '9':
            security_id = int(input("Введите ID ценной бумаги для удаления: "))
            security = Security(security_id, '', '', '', 0)
            security.delete(system.db)
        elif choice == '7':
            client_id = int(input("Введите ID клиента для удаления: "))
            client = Client(client_id, '', '', '', '')
            client.delete(system.db)
        elif choice == '10':
            client_id = int(input("Введите ID клиента для отчета: "))
            client = Client(client_id, '', '', '', '')
            client.get_report(system.db)
        elif choice == '11':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
