# A file to activate the functions
import os
import py_to_sql
import arcive_files
import schedule

# To call this functions you need to have MySQL installed and have a
# database named 'info_3'. The password for the MySQL connection has to be
# changed to your MySQL server password

def call_all():
    ## Create a table
    py_to_sql.create_mysql_table()

    ## Fill data into the table
    py_to_sql.multiple_files()

    ## Move files to archive
    os.chdir('..')
    archive_files.move_to_archive('today\'s_articles', 'archive')

schedule.every().day.at('18:30').do(call_all)   

while True:
    schedule.run_pending()

    
    
    
