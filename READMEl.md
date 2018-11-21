# Udacity | Full Stack Web Developer | Project 1 : Log Analysis
Created by: Ebtihal Abduallah

 # Introduction:
The goal is building an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

 ## Installation:
 ------
* Python
To download Python, check the link below 
[python.org](https://www.python.org/downloads/)

* Postgres
Check the download link below choose regard to your operating system  
[postgresql.org](https://www.postgresql.org/download/)
for windows you can install executable version EDB Postgres
[enterprisedb.com](https://www.enterprisedb.com/)

* Psycopg2
You should download psycopg2 module to connect database to Python
For Windows regard to Python version download the suitable package
http://www.stickpeople.com/projects/python/win-psycopg/
 Note: for Windows the last version support Python 3.6


# Configuration:
------
### Python:
For Windows installation, be sure to check add python to PATH
**Note:** if you miss it you can add it to PATH follow the steps:
•	From control panel , system , advance system settings
On Advanced tab , click on Environment variables   
•	Choose path then Edit, press New , copy the program path usually you will find it on 
C:\Users\Username\AppData\Local\Programs\Python\Python37-32
 

### Postgres:
To start use Database follow the steps:
•	Download **newsdata.sql** file
 [Download it here](https://drive.google.com/open?id=1xlfDl6AX1AAAjA-vkrlwDmCjAYaxlk13)
 Note:You will need to unzip this file after downloading it
•	Open **PgAdmin** program then click on **PostgreSQL11** server, enter the password same one you enter it during installation then the server will be active 
•	Create new database in Postgres with name **news**
•  Restore **newsdata.sql** file to Database news in PgAdmin from Tools menu then chooes Restore
Or
use **Terminal** 
To load the data, cd into the directory you save the file to it and use the command 
```
psql -d news -f newsdata.sql
```
Here's what this command does:
• psql — the PostgreSQL command line program
• -d news — connect to the database named news which has been set up for you
• -f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data
Or
use **SQL Shell** 
•	First enter server data 
```
server:localhost
Database:postgres
Port:5432
Username:postgres
Password:<the password you enter it during installation>
```
•	After create **news** database use connect command 
```
Postgres=#\ connect news
```
•	Import database 
```
news=#psql \i c:\user\username\downloads\newsdata.sql
```
**Note**: To test the database from **PgAdmin** choose news database then from Tool menu choos Query tool, writ SQL statement :
```
SELECT * FROM log 
```

 

# SQL statement:
-----


Most popular 3 articles 
```
CREATE VIEW question_1 AS 
( SELECT articles.title as art_tit , count (log.ip) as num
FROM articles JOIN log ON log.path= concat('/article/',articles.slug)
GROUP BY art_tit
ORDER BY num DESC 
LIMIT 3 
 )
```
Most popular authors 
```
CREATE VIEW question_2 AS (
SELECT authors.name , count (log.ip) as total 
FROM articles JOIN log ON log.path= concat('/article/',articles.slug)
JOIN authors ON authors.id=articles.author
GROUP BY authors.name
ORDER BY total DESC)
```
On which days did more than 1% of requests lead to errors
```
CREATE VIEW all_request AS (
SELECT count(*) as num ,
       date(time) as date
FROM log
GROUP BY date
ORDER BY num DESC )

CREATE VIEW all_error AS (
SELECT count(*) as num , date(time) as date
FROM log
WHERE status !='200 OK'
GROUP BY date
ORDER BY num DESC )

CREATE VIEW error1 AS (
SELECT all_request.date,
       round( (all_error.num)* 100.0/all_request.num,2) as err
FROM all_error,  all_request
WHERE all_error.date = all_request.date  )
```

# Resource: 
------
https://www.postgresql.org/docs/
https://docs.python.org/
http://www.postgresqltutorial.com



