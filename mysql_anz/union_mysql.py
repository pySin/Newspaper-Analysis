## analize MySQL
# Get particular tables from a database and 'union them'

import mysql.connector
import time

database = 'info_3' #name of the working database
localtime = time.localtime(time.time())
year_month = str(localtime.tm_year)+str(localtime.tm_mon) # Year and month for witch the union is made

# Function 1
# get the table names from a particular database
def get_dtb_tables(database_name):
    tables_of_database = '''SHOW TABLES FROM %s''' % database_name

    conn = mysql.connector.connect(user = 'root', password = 'dance',
                                   host = 'localhost')
    cursor = conn.cursor()
    cursor.execute(tables_of_database)
    t_names = cursor.fetchall()
    conn.commit()
    conn.close()
    return t_names

# Function 2
# Clear the fetchall result from MySQL to a normal list
def clear_fetchall_result(fetch_result):
    clear_list = [x[0] for x in fetch_result]
    # print(clear_list)
    return clear_list

# Function 3
# sift and keep only the results from November 2019
def tables_by_month(list_for_sift):
    needed_tables = [x for x in list_for_sift if x[0:11] == 'news_'+year_month]
    return needed_tables

# Function 4
# Create UNION MySQL expresson for n-number of tables / The new thing here is
# that a string line is been created line by line for each table in the UNION
# expression

def union_tables(tables_needed):
    str_time = str(time.time())[-5:]
    union_str = 'CREATE TABLE %s.unions_%s_%s AS ' % (database, year_month, str_time) # construct the CREATE TABLE row of the expression
    for item in tables_needed:
        
        row = 'SELECT * FROM %s.%s UNION ALL ' % (database, item) # construct 
        union_str = union_str+row # the UNION row which repeats for each table

    union_str = union_str[:-11]+';'# remove the last 'UNION ALL' row

    print('Union String:', union_str) # check how the string looks
    
    conn = mysql.connector.connect(user = 'root', password = 'dance',
                                   host = 'localhost')
    cursor = conn.cursor()
    cursor.execute('USE info_2;')
    cursor.execute(union_str)

    conn.commit() # create a connection and activate the constructed string
    conn.close()# MySQL expression
    
    return union_str


# call the functions    
def main():
    dtb_table_names = get_dtb_tables(database)
    clear_tables_list = clear_fetchall_result(dtb_table_names)
    tables_needed = tables_by_month(clear_tables_list)
    get_union_tables = union_tables(tables_needed)

if __name__ == "__main__":
    main()



# fun 1
# fun 2
# class 1
# class 2

# func main
'''
if __name__ == "__main__":
    main()
'''
