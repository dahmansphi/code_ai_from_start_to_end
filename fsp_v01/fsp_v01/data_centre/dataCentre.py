import os
import pprint
import ftplib
import csv
import pandas as pd
import numpy as np
from PIL import Image as im 

from .dbMain import DbMainCls
from fsp_v01.config import config
from ..scrap.scrap import ScrapCls

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# from PySide6.QtWidgets import QApplication, QMainWindow

class DataCentre:
    def __init__(self):
        self.__mainPathToDataCenter = os.getcwd() + '/fsp_v01/data_centre/' # main path to this model

# return all sectors from db
    def return_all_sectors(self):
        '''this function access the db and retern all the sectors from the tabel sectors'''
        inqery_str = config["select_ALL_FROM_sector_table"]
        inst = DbMainCls()
        sectors_data = inst.selectFromTable(case_to_select=inqery_str)
        return(sectors_data)
# return relevant companies based on the clicked sector
    def return_relevant_companies(self, indx):
        inqery_str = config["select_relevant_COM_FROM_SECTOR_COMP"]
        inqery_indx = indx

        sector_tuple_temp = tuple()
        case_sector_data = sector_tuple_temp + (inqery_indx,)

        inst = DbMainCls()
        comps_data = inst.selectFromTable(case_to_select=inqery_str, caseData=case_sector_data)
        return comps_data
# return companies given the indx of that company
    def return_company_give_indx(self,indx):
        inqery_str = config['select_compnies_given_indx_FROM_comp_table']
        inqery_indx = indx

        sector_tuple_temp = tuple()
        case_sector_data = sector_tuple_temp + (inqery_indx,)

        inst = DbMainCls()
        comps_data = inst.selectFromTable(case_to_select=inqery_str, caseData=case_sector_data)
        return comps_data

  
# Pre process to create company fingerprint 
# ******************************************
    def comFingerPrint(self):
        '''This function create img like fingure for a company,
            the strategy is by converting the ONE_YEAR historical price into np array. each day has five main 
            columns, [open,high,low,close,volume] , we add to this extra info: volum diff from avg, close to open diff, etc.
            so the final array will be:
            [open,high,low,close,volume, volum_diff_from_avg,
            close_open_diff_val, high_low_diff_val, close_low_diff_val,
            close_high_diff_val, open_low_diff_val, open_high_diff_val, 
            next_day_open_close_diff, entry_label]
            so it takes the one year list which most probabley would be 250 days, each entry day has 14 data entry,
            the final will be of size(250,14) shape. 
        '''
        filePath = self.__mainPathToDataCenter + 'THYAO_ONEYEAR.csv'
        df = pd.read_csv(filePath)
        df = df.iloc[::-1].reset_index(drop=True)
        df['Volume'] = df['Volume'].str.replace(',','').astype(float) # make sure to convert the volume entry into float

        numChunk = int(len(df)/5)
        df_np = df.iloc[:,1:].to_numpy() # convery to np array from pd DataFrame
       
        avgVolum = (np.sum(df_np[:,4]))/len(df_np) # find avg volum of the entire year
        append_list_np = []

        # add the volum factor 
        indx = 1
        next_day_close_to_open_diff = None
        for itm in df_np:
            if indx < len(df_np):
                open_next_price = df_np[indx][0]
                close_next_price = df_np[indx][3]
                next_day_close_to_open_diff = close_next_price - open_next_price
            else:
                next_day_close_to_open_diff = 0
                

            open_price = itm[0]
            high_price = itm[1]
            low_price = itm[2]
            close_price = itm[3]

            vol_from_avg_val = itm[4] - avgVolum # capture different between curr volum and avg volum 
            close_open_diff_val = close_price - open_price # capture diffrent between close and open
            high_low_diff_val = high_price - low_price # capture the diff between high and low price

            close_low_diff_val = close_price - low_price # capture close to low price diff
            close_high_diff_val = close_price - high_price # capture close to high price diff
            open_low_diff_val = open_price - low_price # capture open to low price diff
            open_high_diff_val = high_price - open_price  # capture open to high price diff

            entry_label = 0 if close_open_diff_val<0 else 1
            
            # append them all
            arr_temp = np.array([vol_from_avg_val, close_open_diff_val,high_low_diff_val,
                                 close_low_diff_val, close_high_diff_val,
                                 open_low_diff_val, open_high_diff_val, next_day_close_to_open_diff,
                                 entry_label])
            
            append_list_np.append(arr_temp)
            
            indx+=1
        
        append_list_np = np.array(append_list_np)
        df_np = np.hstack((df_np, append_list_np))
        
        return df_np
    
    def save_img_companyFingerPrint(self):
        
        positive_label_folder = self.__mainPathToDataCenter + 'positive_label'
        negative_label_folder = self.__mainPathToDataCenter + 'negative_label'
        
        df_THYAO_price_history = self.comFingerPrint()
        indx = 0
        for itm in df_THYAO_price_history:
            itm_label = itm[-1]
            name_case_indx = str(indx)
            if itm_label == 0.0:
                img = self.return_img(arr=itm)
                name_case = negative_label_folder +'/negative_' + name_case_indx + '.jpeg'
                img.save(name_case)
                
            else:
                img = self.return_img(arr=itm)
                name_case = positive_label_folder + '/positive_' + name_case_indx + '.jpeg'
                img.save(name_case)

            indx += 1

    def return_img(self, arr):
        imgArray = (arr * 255 / np.max(arr)).astype('uint8')
        img = im.fromarray(imgArray)
        return img


# Pre process to create sector, company and relation ds and json
# *******************************************
    def insert_toDB_sector_comp(self):
        ''' In this function we have inserted into the sector_comp tabel the many2many relations
          that company belong to many sectors, and sector have many comapy '''
        inst = ScrapCls()
        instDB = DbMainCls()
        IST_DATA = inst.returnIST_JSON()

        case_to_insert = config["insert_INTO_sector_comp_table"]

        select_sector_id = config["select_FROM_sector_table"]
        select_comp_id = config["select_FROM_comp_table"]

        for itm in IST_DATA:
            sect_Name_val_inquery = itm['Sector']
            sector_temp_tuple = tuple()
            sector_temp_tuple = sector_temp_tuple + (sect_Name_val_inquery,)

            SectordataID = instDB.selectFromTable(case_to_select=select_sector_id, caseData=sector_temp_tuple)
            SectordataID = SectordataID[0][0]
            
            sect_companies_list = itm['Companies']
            for comp in sect_companies_list:
                if type(comp) is dict:
                    comp_name_val_inquery = comp['code']
                    comp_temp_tuple = tuple()
                    comp_temp_tuple = comp_temp_tuple + (comp_name_val_inquery,)
                    CompanydataID = instDB.selectFromTable(case_to_select=select_comp_id, caseData=comp_temp_tuple)
                    CompanydataID = CompanydataID[0][0]

                    case_sector_comp_data = tuple()
                    case_sector_comp_data = case_sector_comp_data + (SectordataID, CompanydataID,)
                    instDB.insertIntoTable(case_to_insert=case_to_insert, caseData=case_sector_comp_data)
            
        print("Insert into sector_comp tabel has been successful")

        # pprint.pprint(IST_DATA[1])

    def insert_toDB_companies(self):
        ''' In this function we have inserted all companies that are in companies.json into the DB '''
        companyPATHsector = self.__mainPathToDataCenter + "companies.json"
        inst = ScrapCls()
        companyDATA = inst.serializerLOAD_JSON(file_path=companyPATHsector) # raw data of all companies read from the json file
        case_to_insert = config["insert_INTO_company_table"] # use config to read the insert sentence
        instDB = DbMainCls()
        try:
            for itm in companyDATA:
                for k, v in itm.items():
                    company_tuple_temp = tuple()
                    case_company_data = company_tuple_temp + (v, k,)
                    instDB.insertIntoTable(case_to_insert=case_to_insert, caseData=case_company_data)
            
            print("Insert of all companies to DB has been successful")

        except Exception as e:
            print(f"inser NOT GOOD, {e}")
                             
    def insert_toDB_sectors(self):
        ''' In this function we have inserted all sectors that are in sectors.json into the DB '''
        sectorPathJSON = self.__mainPathToDataCenter + "sectors.json"
        inst = ScrapCls()
        sectorDATA = inst.serializerLOAD_JSON(file_path=sectorPathJSON) # raw data of all sectors read from the json file
        
        case_to_insert = config["insert_INTO_sector_table"] # use config to read the insert sentence
        instDB = DbMainCls()
        try:
            for sector in sectorDATA:
                sector_tuple_temp = tuple()
                case_sector_data = sector_tuple_temp + (sector,)

                instDB.insertIntoTable(case_to_insert=case_to_insert, caseData=case_sector_data)
            print("Insert of all sector to DB has been successful")
        except Exception as e:
            print(f"could not insert, {e}")

    def createRT_price(self):
        '''This is one time function to create list of historical price close ONLY
            the historical list will be used to stream real time price data
        '''
        df = pd.read_csv(self.__mainPathToDataCenter + 'THYAO_ONEYEAR.csv')
        df.set_index('Date')
        df = df.iloc[::-1].reset_index(drop=True)
        
        fieldname = ['RT_price']
        file_path = self.__mainPathToDataCenter + 'THYAO_RT_PRICE.csv'
        
        # # ## create the original price csv file that will be streamed
        # with open(file_path, 'w') as csv_file:
        #     csv_write = csv.DictWriter(csv_file, fieldnames=fieldname)
        #     csv_write.writeheader()

        # ## write the existing historical info to the list
        # with open(file_path, 'a') as csv_file:
        #     csv_write = csv.DictWriter(csv_file, fieldnames=fieldname)
        #     for inx in range(len(df['Date'])):
        #         info = {
        #             'RT_price': df['Close'][inx]
        #             }
        #         csv_write.writerow(info)
        
    def createSectorListJSON(self):
        '''this function create list of all sectors in IST, it takes the raw data from the IST_List.json in scrap model
            it output a json file sectors.json
        '''
        inst = ScrapCls()
        data = inst.returnIST_JSON() # row data is here check the scrap class to see the structure of that data

        sectorNames_LIST = [] # this will hold the final call
        for itm in data:
            sectorName = itm['Sector']
            sectorNames_LIST.append(sectorName)

        sectorNamesJSON = self.__mainPathToDataCenter + 'sectors.json'
        inst.serializerSAVE_JSON(pathToSAVE_TO_JSON_extention=sectorNamesJSON, sourceTOread_FROM_LIST_TYPE=sectorNames_LIST)
        print("sectors are saved in JSON")
    
    def createCompanies(self):
        '''this function create list of all companies in IST, no redundent of the company name, there are all unique
            it takes the raw data from the IST_List.json in scrap model
            it output a json file companies.json that hold the company name and the code of the company
        '''
        inst = ScrapCls()
        data = inst.returnIST_JSON()

        companies_lst = []
        for itm in data: # loop over the raw data, that have two keys Companies and Sector, 
            for recod in itm['Companies']: # we need to loop only over the Companies
                dicTemp = {} # to hold a temp dict that will be later append to companies_lst
                if type(recod) is dict: # just make sure that the current record have companies, otherwise the sector have no copmanies
                    code = recod['code']
                    company = recod['company']
                    dicTemp[code] = company
                if dicTemp: #make sure that the json file will not hold empty dic that is the first one
                    IsIn = dicTemp in companies_lst
                    if IsIn == False:
                        companies_lst.append(dicTemp)
           
        uniqCompaniesNamesJSON = self.__mainPathToDataCenter + 'companies.json'
        inst.serializerSAVE_JSON(pathToSAVE_TO_JSON_extention=uniqCompaniesNamesJSON, sourceTOread_FROM_LIST_TYPE=companies_lst)
        print("companies are saved in JSON")


