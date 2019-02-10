import sqlite3 as sql
from sqlite3 import Error
import os

tables_nonpets = ('expense', 'images', 'meds', 'stats', 'vet')


def create_connection(db_file="pets.db"):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


def insert_record(tablename, values_):
    conn = create_connection()
    c = conn.cursor()

    keys = ','.join(values_.keys())
    question_marks = ','.join(list('?'*len(values_)))
    data_ = tuple(values_.values())
    
    c.execute('INSERT INTO '+tablename+' ('+keys+') VALUES ('+question_marks+')', data_)
    conn.commit()
    conn.close()


def delete_records(tablename, column_, value_):
    # when deleting a pet all related records in other tables will be deleted
    conn = create_connection()
    c = conn.cursor()
    
    c.execute('DELETE FROM '+ tablename +' WHERE ' + column_ + ' = ' + value_)
    
    for t in tables_nonpets:
        c.execute('DELETE FROM '+ t +' WHERE id = ' + value_)
    
    conn.commit()
    conn.close()


def delete_record_from_table(tablename, column_, value_):
    # for non-pets tables --> pass the record id / to delete all records for pet, delete from pets table
    conn = create_connection()
    c = conn.cursor()
    
    c.execute('DELETE FROM '+ tablename +' WHERE ' + column_ + ' = ' + value_)
    
    conn.commit()
    conn.close()


def find_records(tablename, pet_id):
    conn = create_connection()
    c = conn.cursor()

    if tablename == 'pets':
        c.execute('SELECT * FROM '+ tablename +' WHERE id = ' + str(pet_id))
    else:
        c.execute('SELECT * FROM '+ tablename +' WHERE id = ' + str(pet_id) + ' ORDER BY date DESC')
    results = c.fetchall()
    conn.close()
    return results

# test = ""
# field_ = ""
# data_to_enter = {}
# continue_ = ""

# test = input("start? ")

#find data
print(find_records('vet', 7))

#delete data
# while test != "N":
#     table_ = input("Which Table to delete from? ")
#     column_ = input("Which Column - use id? ")
#     value_ = input ("record to delete matches: ")

#     delete_record(table_, column_, value_)

#     test = input("again? ")

#add data
# while test != 'n':
#     tablename = input("Table name: ")

#     while continue_ != "y":
#         print("new field record --------- N to fin")
#         field_ = input("table column: ")
#         value_ = input("input value: ")
#         data_to_enter[field_] = value_
#         continue_ = input("done? ")
    
#     keys = ','.join(data_to_enter.keys())
#     question_marks = ','.join(list('?'*len(data_to_enter)))
#     values = tuple(data_to_enter.values())
    
#     print('INSERT INTO '+tablename+' ('+keys+') VALUES ('+question_marks+')', values)
#     insert_record(tablename, data_to_enter)
#     test = input("more? ")

