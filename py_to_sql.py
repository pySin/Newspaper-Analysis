# Python to MySQL connection

import mysql.connector
import text_anz_functions

get_list = text_anz_functions.word_frequency('text.txt')
most_pop_20 = get_list[0:20]


## Create MySQL table with nested list 
def create_mysql_table(table_name):

    column_names = []

    for item in most_pop_20:
        column_names.append(item[1]+'_'+' VARCHAR(100)') # using underscore to
                                          # avoid the words reserved for MySQL

    # create a string to be interpreted by the MySQL server
    list_to_mysql_str = """CREATE TABLE %s(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       %s);""" % (table_name, column_names)

    # remove some symbols
    list_to_mysql_str_2 = list_to_mysql_str.replace('[', '')
    list_to_mysql_str_3 = list_to_mysql_str_2.replace(']', '')
    list_to_mysql = list_to_mysql_str_3.replace('\'', '')
    
    print(list_to_mysql) # check how the string looks

    # connect to database
    conn = mysql.connector.connect(user = 'root', password = 'your_password',
                                   host = 'localhost')
    cursor = conn.cursor()
    cursor.execute(list_to_mysql)    

    conn.commit()
    conn.close()

# create_mysql_table('info_3.text_top_20') # 'info_3' - database name
                                           # 'text_top_20' - table name

## Populate mysql table function

def populate_mysql_table(table_name):

    column_names = []
    column_values = []

    for item in most_pop_20:
        column_names.append(item[1]+'_') # using underscore to avoid the words
        column_values.append(item[0]) # reserved for MySQL

    list_to_mysql_str = """INSERT INTO %s(id, %s)
                       VALUES(NULL, %s);""" % (table_name, column_names,
                                               column_values)

    list_to_mysql_str_2 = list_to_mysql_str.replace('[', '')
    list_to_mysql_str_3 = list_to_mysql_str_2.replace(']', '')
    list_to_mysql = list_to_mysql_str_3.replace('\'', '')
    
    print(list_to_mysql)

    
    conn = mysql.connector.connect(user = 'root', password = 'your_password',
                                   host = 'localhost')
    cursor = conn.cursor()
    cursor.execute(list_to_mysql)    

    conn.commit()
    conn.close()
    

populate_mysql_table('info_3.text_top_20')

