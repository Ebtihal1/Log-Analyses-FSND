#!/usr/bin/env python3

import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(database="news",
                        user="postgres", password="google",
                        host="localhost", port="5432")

print ("opened database successfully")

cursor = conn.cursor()

# Most populer articles
cursor.execute(" SELECT articles.title as art_tit,count (log.ip) as num \
                FROM articles JOIN log ON \
                log.path = concat('/article/' , articles.slug) \
                GROUP BY art_tit \
                ORDER BY num DESC \
                LIMIT 3 ")

rows = cursor.fetchall()
print("\nthe most poupluer aricales\n")
for i in range(len(rows)):
        art_tit = rows[i][0]
        num = rows[i][1]

        print(" Title: %s" % (art_tit) + "--""Views: %s" % (num))

# Most populer authors
cursor.execute(" SELECT authors.name,count (log.ip) as total \
                FROM articles JOIN log ON \
                log.path = concat('/article/' , articles.slug) \
                JOIN authors ON authors.id = articles.author \
                GROUP BY authors.name \
                ORDER BY total DESC ")

rows = cursor.fetchall()
print("\nthe most poupluer authors\n")
for i in range(len(rows)):
        name = rows[i][0]
        total = rows[i][1]

        print("Author: %s" % (name) + "--""Views: %s" % (total))

# Error request date
cursor.execute("SELECT * FROM error1 WHERE err > 1.0 ")

rows = cursor.fetchall()
print("\n requests lead to errors\n")
for i in range(len(rows)):
        date = rows[i][0]
        error = rows[i][1]

        print("Date: %s" % (date) + "--""Error: %f" % (error))

print ("\nOperation done succefully")
conn.close()
