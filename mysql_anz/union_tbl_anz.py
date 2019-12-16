# Analize Union Table 19/11/2019
import time
import mysql.connector

# Sift the UNION result table to keep only the labour records / Create
# MySQL command string with custom new table name /
# sift rows not containing '$p' as well to get only the percent records.
# The names of the articles in the table that calculate percentages are marked
# with '$percent'
time_now = time.localtime(time.time())

# Function 1
# Labour Sift / keep only the labour newspaper records
def labour_sift(database, source_table_name):
    new_table_name = database+'.news_labour_formula_'+str(time_now.tm_year)+str(time_now.tm_mon)+str(time_now.tm_mday)
    labour_sift_str = """
                      CREATE TABLE %s AS
                      WITH labour_sift AS(
                      SELECT * FROM %s
                      WHERE website = 'https://www.independent.co.uk' 
                      OR website = 'https://www.mirror.co.uk'
                      OR website = 'https://www.theguardian.com'
                      ) SELECT * FROM labour_sift WHERE title REGEXP '[$]p';
                      """ % (new_table_name, source_table_name)

    print(labour_sift_str)
    conn = mysql.connector.connect(user = 'root', password = 'dance',
                                   host = 'localhost')
    cursor = conn.cursor()
    cursor.execute(labour_sift_str)

    conn.commit()
    conn.close()

# Function 2
# Conservative sift / keep only the conservative newspaper recods
def conservative_sift(database, source_table_name):
    new_table_name = database+'.news_conservative_formula_'+str(time_now.tm_year)+str(time_now.tm_mon)+str(time_now.tm_mday)
    labour_sift_str = """
                      CREATE TABLE %s AS
                      WITH labour_sift AS(
                      SELECT * FROM %s
                      WHERE website = 'https://www.express.co.uk' 
                      OR website = 'https://www.dailymail.co.uk'
                      OR website = 'https://www.telegraph.co.uk'
                      ) SELECT * FROM labour_sift WHERE title REGEXP '[$]p';
                      """ % (new_table_name, source_table_name)

    print(labour_sift_str)
    conn = mysql.connector.connect(user = 'root', password = 'dance',
                                   host = 'localhost')
    cursor = conn.cursor()
    cursor.execute(labour_sift_str)

    conn.commit()
    conn.close()


def main():
    labour_sift('info_3', 'info_3.unions_201911')
    conservative_sift('info_3', 'info_3.unions_201911')

if __name__ == '__main__':
    main()

