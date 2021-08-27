# dublicate-remover-from-mysql-slow-query-log
Parse MySQL log slow queries and print filtered unique queries

test: msqldr.py /var/log/mysql/slow-queries.log > filtered-slow-queries.log
