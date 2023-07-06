Файл books.json сформирован командой:
python manage.py dumpdata books.book > fixtures/books.json

Для загрузки, необходимо выполнить в терминале:
python manage.py loaddata fixtures/books.json