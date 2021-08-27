# dublicate-remover-from-mysql-slow-query-log
Parse MySQL log slow queries and print filtered unique queries

Скрипт для анализа лог файла медленных MySQL запросов. Ищет по указанному пути лог файл, выводит уникальные строки запросов.

К статье [Оптимизация сервера](https://vk.com/@sozdanie_prodvijenie_marketing-optimizaciya-servera)

test: msqldr.py /var/log/mysql/slow-queries.log > filtered-slow-queries.log
