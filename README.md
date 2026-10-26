# Информационная система инвестиционной компании

![SQL](https://img.shields.io/badge/SQL-Access_%7C_SQLite-003B57?logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/Python-sqlite3-3776AB?logo=python&logoColor=white)
![UML](https://img.shields.io/badge/UML-draw.io-F08705?logo=diagramsdotnet&logoColor=white)
![BMSTU](https://img.shields.io/badge/МГТУ_им._Баумана-ИУ1-0a4a8f)

Сквозной учебный проект по базам данных и моделированию информационных систем: от модели предметной области до работающего приложения.
7 семестр, группа ИУ1-72Б, кафедра ИУ1, МГТУ им. Н.Э. Баумана (осень 2024).

**Предметная область.** Компания ведёт клиентов-предприятий, их инвестиционные проекты и ценные бумаги, в которые вложены проекты (связь «многие ко многим» через таблицу «Сведения о проекте»).

## Что внутри

| Этап | Файлы | Содержание |
|---|---|---|
| Функциональная модель и ER | [`diagrams/idef0-and-er.drawio`](diagrams/idef0-and-er.drawio) | IDEF0-модель работы аналитического центра и ER-диаграмма |
| Варианты использования | [`use-case.drawio`](diagrams/use-case.drawio), [`use-case.png`](diagrams/use-case.png), [`use-case-scenarios.drawio`](diagrams/use-case-scenarios.drawio) | акторы «Клиент» и «Аналитик», сценарий «Управление инвестициями» с альтернативными потоками |
| Кооперация и классы | [`collaboration.drawio`](diagrams/collaboration.drawio), [`collaboration-and-classes.png`](diagrams/collaboration-and-classes.png), [`class-diagram.drawio`](diagrams/class-diagram.drawio) | диаграмма сотрудничества для добавления проекта, диаграмма классов |
| База данных Access | [`database/investments.accdb`](database/investments.accdb) | та же схема, реализованная в MS Access |
| SQL | [`database/queries.sql`](database/queries.sql) | `CREATE`/`DROP` всех таблиц, выборки с `WHERE`, `ORDER BY`, агрегатами, `GROUP BY … HAVING`, `UNION`, `INTERSECT` |
| Приложение | [`app/investment_system.py`](app/investment_system.py) | консольное CRUD-приложение на Python + SQLite: клиенты, проекты, ценные бумаги, отчёт по клиенту |

## Схема данных

```
Клиент (ID Клиента, Название предприятия, Вид собственности, Адрес, Телефон)
   │ 1
   │ N
Инвестиционный проект (ID Проекта, Название, Сумма инвестиций, Дата начала, Дата завершения, ID Клиента)
   │ M                                   N │
   └──── Сведения о проекте (ID Проекта, ID Ценной бумаги) ────┘
                                           │
Ценные бумаги (ID Ценной бумаги, Тип, Дата выпуска, Дата погашения, Доходность)
```

## Запуск приложения

```bash
python app/investment_system.py
```

При первом запуске создаётся файл `investment_system.db` с таблицами, дальше работа идёт через текстовое меню.
Тот же код с результатом запуска лежит в ноутбуке [`app/investment_system.ipynb`](app/investment_system.ipynb).

## Автор

Салженикин Даниил, МГТУ им. Н.Э. Баумана.
