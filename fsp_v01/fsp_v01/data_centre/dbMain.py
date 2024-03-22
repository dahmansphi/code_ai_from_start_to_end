import os
from pathlib import Path
import sqlite3

# dbDirPath = os.getcwd()
dbDirPath = os.path.dirname(os.path.abspath(__file__))

class DbMainCls:
    def __init__(self) -> None:
        pass
    
    def createDBandTabel(self):
#         ''' To be executed only one time as the starting of the app, in order to create the DB and the relevant table'''
        try:
            str_create_tabel_sector= '''CREATE TABLE IF NOT EXISTS SECTORS
                                (
                                    id integer PRIMARY KEY,
                                    SECTOR_NAME  TEXT  NOT NULL
                                );'''
            str_create_tabel_company= '''CREATE TABLE IF NOT EXISTS COMPANIES
                                (
                                    id integer PRIMARY KEY,
                                    COMPPANY_NAME  TEXT    NOT NULL,
                                    COMPPANY_CODE  TEXT    NOT NULL
                                );'''
            str_create_tabel_sector_company= '''CREATE TABLE IF NOT EXISTS SECTOR_COMP
                                (
                                    id integer PRIMARY KEY,
                                    SECTOR_ID  INTEGER,
                                    COMPPANY_ID  INTEGER
                                );'''
#             # create the DB
            sqlConn = sqlite3.connect(dbDirPath + '/' +'DBfsp_v01.db')
            cursor = sqlConn.cursor()

            cursor.execute(str_create_tabel_sector)
            cursor.execute(str_create_tabel_company)
            cursor.execute(str_create_tabel_sector_company)

            print('successful connection and creation of tabels')
        except sqlite3.Error as e:
            print(f'Fail as try to connect: {e}')
        finally:
            if sqlConn:
                sqlConn.close()
                print("The sqlite connection is closed")


    def insertIntoTable(self, case_to_insert, caseData):
        '''this function act to insert into the db, requires two args, case to insert in str, and the data'''
        try:
            sqlConn = sqlite3.connect(dbDirPath + '/' +'DBfsp_v01.db')
            with sqlConn:
                cursor = sqlConn.cursor()
                cursor.execute(case_to_insert, caseData)
                sqlConn.commit()
                # print("case is inserted")
        except sqlite3.Error as e:
            print(f"error in insertingas {e}")

    def selectFromTable(self, case_to_select, caseData=None):
        try:
            sqlConn = sqlite3.connect(dbDirPath + '/' +'DBfsp_v01.db')
            if caseData:
                with sqlConn:
                    cursor = sqlConn.cursor()
                    cursor.execute(case_to_select, caseData)
                    row = cursor.fetchall()
                    return row
            else:
                with sqlConn:
                    cursor = sqlConn.cursor()
                    cursor.execute(case_to_select)
                    row = cursor.fetchall()
                    return row
        except sqlite3.Error as e:
            print(f"error in selectFrom function {e}")

