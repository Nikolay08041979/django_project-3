# Домашнее задание №3 "Работа с ORM"

## [Выгрузка каталога товаров из csv-файла с сохранением всех позиций в базе данных.](https://github.com/netology-code/dj-homeworks/tree/video/2.1-databases/work_with_database)

### Функционал:

✅ Загружены все данные из [csv файла](https://github.com/Nikolay08041979/django_project-3/blob/master/2.1-databases/work_with_database/phones.csv) в БД posgresql

✅ Выдача страницы по адресу http://127.0.0.1:8000/catalog/ должна полностью соответствовать [макету](https://github.com/Nikolay08041979/django_project-3/blob/master/2.1-databases/work_with_database/res/catalog.png)

✅ Сортировка по убыванию/возрастанию цены

✅ Сортировка по названию


### Измененя внесены:
✅ [phone/modele.py](https://github.com/Nikolay08041979/django_project-3/blob/master/2.1-databases/work_with_database/phones/models.py)

✅ [management/commands/import_phones.py](https://github.com/Nikolay08041979/django_project-3/blob/master/2.1-databases/work_with_database/phones/management/commands/import_phones.py)

✅ [phones/views.py](https://github.com/Nikolay08041979/django_project-3/blob/master/2.1-databases/work_with_database/phones/views.py)

✅ [phones/admin.py](https://github.com/Nikolay08041979/django_project-3/blob/master/2.1-databases/work_with_database/phones/admin.py)

✅ [main/settings.py](https://github.com/Nikolay08041979/django_project-3/blob/master/2.1-databases/work_with_database/main/settings.py): изменены учетные данные для доступа к postgresql

## [Делаем онлайн-библиотеку](https://github.com/netology-code/dj-homeworks/tree/video/2.1-databases/models_list_displaying)