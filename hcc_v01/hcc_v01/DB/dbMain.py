import os
from pathlib import Path
import sqlite3

# dbDirPath = os.getcwd()
dbDirPath = os.path.dirname(os.path.abspath(__file__))


class DbMainCls:
    # def __init__(self) -> None:
    #     pass
    
    def createDBandTabel(self):
        ''' To be executed only one time as the starting of the app, in order to create the DB and the relevant table'''
        try:
            str_create_tabel= '''CREATE TABLE IF NOT EXISTS PATIENTTABEL(
                                id integer PRIMARY KEY,
                                IMG_IDNAME  TEXT    NOT NULL,
                                AGE INT NOT NULL,
                                DESCRIBTION CHAR(50),
                                IMG_CASE BLOB,
                                PATIENT_STAT INTEGER);'''
            # create the DB
            sqlConn = sqlite3.connect(dbDirPath + '/' +'DBhcc_v01.db')
            cursor = sqlConn.cursor()
            cursor.execute(str_create_tabel)
            print('successful connection and creation of tabel')
        except sqlite3.Error as e:
            print(f'Fail as try to connect: {e}')
        finally:
            if sqlConn:
                sqlConn.close()
                print("The sqlite connection is closed")

    def insertIntoTable(self, patientData):
        try:
            case_to_insert = """
                        INSERT INTO PATIENTTABEL
                        (
                            IMG_IDNAME,
                            AGE,
                            DESCRIBTION,
                            IMG_CASE,
                            PATIENT_STAT
                        )  
                          VALUES  (?,?,?,?,?)
                          """
            sqlConn = sqlite3.connect(dbDirPath + '/' +'DBhcc_v01.db')
            with sqlConn:
                cursor = sqlConn.cursor()
                cursor.execute(case_to_insert, (patientData[0],patientData[1],patientData[2],patientData[3],patientData[4]))
                sqlConn.commit()
                print("case is inserted")
        except sqlite3.Error as e:
            print(f"error in insertingas {e}")

    def selectFromTable(self, val):
        try:
            case_to_select = """
                        SELECT * FROM PATIENTTABEL WHERE id =?
                        """
            sqlConn = sqlite3.connect(dbDirPath + '/' +'DBhcc_v01.db')
            with sqlConn:
                cursor = sqlConn.cursor()
                cursor.execute(case_to_select, (val,))
                row = cursor.fetchall()
                return row
        except sqlite3.Error as e:
            print(f"error in selectFrom function {e}")

    def selectALLFromTable(self):
        try:
            case_to_select = """
                        SELECT * FROM PATIENTTABEL
                        """
            sqlConn = sqlite3.connect(dbDirPath + '/' +'DBhcc_v01.db')
            
            with sqlConn:
                cursor = sqlConn.cursor()
                cursor.execute(case_to_select)
                row = cursor.fetchall()
                return row
        except sqlite3.Error as e:
            print(f"error in selectALL function {e}")

    def selectLASTFromTable(self):
        try:
            case_to_select = """
                        SELECT * FROM PATIENTTABEL ORDER BY rowid DESC LIMIT 1;
                        """
            sqlConn = sqlite3.connect(dbDirPath + '/' +'DBhcc_v01.db')
            with sqlConn:
                cursor = sqlConn.cursor()
                cursor.execute(case_to_select)
                row = cursor.fetchall()
                return row
        except sqlite3.Error as e:
            print(f"error in selectLAST function {e}")
    
    def deletFromTable(self,val):
        try:
            case_to_select = """
                        DELETE FROM PATIENTTABEL WHERE id =?
                        """
            sqlConn = sqlite3.connect(dbDirPath + '/' +'DBhcc_v01.db')
            with sqlConn:
                cursor = sqlConn.cursor()
                cursor.execute(case_to_select, (val,))
                sqlConn.commit()
                print("case is deleted")
        except sqlite3.Error as e:
            print(f"error in delet function {e}")

    
    def deletALLFromTable(self):
        try:
            case_to_select = """
                        DELETE FROM PATIENTTABEL
                        """
            sqlConn = sqlite3.connect(dbDirPath + '/' +'DBhcc_v01.db')
            with sqlConn:
                cursor = sqlConn.cursor()
                cursor.execute(case_to_select)
                sqlConn.commit()
                print("All cases are deleted")
        except sqlite3.Error as e:
            print(f"error in delet ALL function {e}")






# #format to create the main DB and table if not exist
# DbMainCls().createDBandTabel()
# ****************************************
# format to insert it's needed in this form of lisit
# with open("p3.jpeg","rb")as f:
#     dataIMG = f.read()
# caseP = [
#     'imgid0033', 50, 'he is ok', dataIMG, 0
# ]
# DbMainCls().insertIntoTable(patientData=caseP)
# ***********************************
# # format to select specific case
# row = DbMainCls().selectFromTable(val=2)
# # print(row)
# for itm in row:
#     print(itm[4])
# with open("testRR.gif", "wb") as f:
#     f.write(img)
# ************************************
# format to select ALL from the table
# row = DbMainCls().selectALLFromTable()
# print(row[0][1]) 
# **************************

# select the last record in db
# row = DbMainCls().selectLASTFromTable()
# print(row[0][0])

# ***********************************
# # format to delete from db
# DbMainCls().deletFromTable(val=0)
# # format to delete all from db
# DbMainCls().deletALLFromTable()