# Introduction
Scraping articles from news websites and looking for language patterns in the text.
Recognise narrative styles and create profiles for the most popular styles.

Newspapers to Analyse:
Analyse newspapers by their political inclination

Neutral = Google News, BBC

Left: The guardian, Daily Mirror, The independent

Right: The Daily Telegraph, Daily Express, Daily Mail

# Technologies

1. Python - mysql.connector, re, datetime, os
2. MySQL

# Tasks
## 1. Scraping 
###	a) website
###	b) article URL
###	c) header
###	d) article content
###	e) separate paragraphs

## 2. Text analysis
###	a) word frequency (excluding prepositions and most common words)
###	b) parts of speech analysis
###		b.a) adjectives analysis
			b.a.a) adjectives frequencies
###		b.b) adverbs analysis
			b.b.a) adverbs frequencies
###		b.c) conjunctions analysis
			b.c.a) conjunctions frequencies
###		b.d) interjections analysis
			b.d.a) interjections frequencies
###		b.e) nouns analysis
			b.e.a) nouns frequencies
###		b.f) prepositions analysis
			b.f.a) prepositions frequencies
###		b.g) pronouns analysis
			b.g.a) pronouns frequencies
###		b.h) verbs analysis
####			b.h.a) verbs frequencies

## 3. Transfering the data into a database or tabular data files(CSV, excel)

# Setup

1. Create 2 sub-folders in your main folder. The furst folder(today's_articles) is for the articles that we'll analyse. The second folder(archives) is for the articles we have already analysed. Place some .txt files with articles in "today's_articles" for analysis.
2. Set MySQL community or corporate server.
3. In 'py_to_sql.py' file the following expression - "cursor.execute('USE info_3;')" - is used 3 times. 'info_3' is the MySQL database where the new table will be created and populated with data. Change the name 'info_3' with your database name in all 3 places.
4. Use your own password when connecting to the database - /conn = mysql.connector.connect(user = 'root', password = 'your_password',
                                   host = 'localhost')/ 3 times
5. Run 'function_call.py' file.

We are open to any new tasks that might be interesting to you! 
