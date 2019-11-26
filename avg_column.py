# Average for every column in a MySQL table
import mysql.connector

# Get the column  names from a table
# Needs table name and connection to MySQL database

table_name = 'info_3.news_labour_formula_20191126'

def get_columns_names(table_name):
    split_name = table_name.split('.')
    database = split_name[0]
    table = split_name[1]
    query_column_names = """
                        SELECT
                            COLUMN_NAME DATA_TYPE
                        FROM
                            INFORMATION_SCHEMA.COLUMNS
                        WHERE
                            TABLE_SCHEMA = \'%s\'
                        AND
                            TABLE_NAME = \'%s\'; 
                         """ % (database, table) # MySQL expression 
    print(split_name)
    print(query_column_names)

    conn = mysql.connector.connect(user = 'root', password = 'dance',
                                   host = 'localhost')
    cursor = conn.cursor()
    cursor.execute(query_column_names)
    get_columns = cursor.fetchall()

    conn.commit()
    conn.close()
    return get_columns

# Create columns names list from the fetchall result

def clear_fetchall_result(get_columns):
    clear_list_x = [x[0] for x in get_columns]
    clear_list = [x for x in clear_list_x if '_' in x]
    return clear_list

# Create a mysql expression that calculates all the average numbers for
 # each column / needs table name and list of the column names
import time

def mysql_col_avg(table_name, clear_list):
    # get database name for table name construction
    split_name = table_name.split('.')
    database = split_name[0]

    # get the names 'labour' or 'conservative' depending on the table analised
    labour_or_cons = []
    if 'labour' in table_name:
        labour_or_cons.append('"labour"')
    elif 'conservative' in table_name:
        labour_or_cons.append('"conservative"')
    else:
        print('Error: Labour or Conservative not in the name!')

    # create table name for the new table
    localtime = time.localtime(time.time())
    avg_table_name = 'avg_'+str(localtime.tm_year)+str(localtime.tm_mon)+'_'+str(time.time())[-5:]

    prepared_list = ['AVG('+str(x)+')' for x in clear_list]

    # main query sent to SQL
    avg_col_query = """
                    CREATE TABLE %s.%s AS
                    SELECT id, dates, %s, %s
                    FROM %s; 
                    """ % (database, avg_table_name, labour_or_cons[0],
                           prepared_list, table_name)

    query_1 = avg_col_query.replace('\'', '')
    query_2 = query_1.replace('[', '')
    query_3 = query_2.replace(']', '')

    print(query_3)

    conn = mysql.connector.connect(user = 'root', password = 'dance',
                                   host = 'localhost')
    cursor = conn.cursor()
    cursor.execute('USE info_2;')
    cursor.execute(query_3)

    conn.commit()
    conn.close()

# Call the functions
def main():
    get_columns = get_columns_names(table_name)
    clear_list = clear_fetchall_result(get_columns)
    mysql_col_avg(table_name, clear_list)

if __name__ == '__main__':
    main()
    
