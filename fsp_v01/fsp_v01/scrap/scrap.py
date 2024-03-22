import requests
from bs4 import BeautifulSoup
from fsp_v01 import config
import os
import json

class ScrapCls:
    def __init__(self):
        pass

    def returnIST_JSON(self):
        ''' this function return KAP data about IST companies by sector, stored in json file, the JSON file was created
            by scrapKAP(url) function
        '''
        file_path = os.getcwd() + '/fsp_v01/scrap/' +  'IST_List.json'
        data = self.serializerLOAD_JSON(file_path=file_path)
        return data
    
    def serializerSAVE_JSON(self, sourceTOread_FROM_LIST_TYPE, pathToSAVE_TO_JSON_extention):
        '''function to save json file format'''
        try:
            with open(pathToSAVE_TO_JSON_extention, "w", encoding='utf-8') as final:
                json.dump(sourceTOread_FROM_LIST_TYPE, final, ensure_ascii=False)
        except Exception as e:
            print(f"err {e}")

    def serializerLOAD_JSON(self, file_path):
        ''' function to load json file format'''
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                data = json.load(f)
                return data
        except:
            return "somthing is wrong, check scap.py the serializerLOAD_JSON function"

    def scrapKAP(self,url):
        ''' This simple function to scrap KAP site looking to extract all IST companies organized by their sectors
            final outcome of this will be a JSON object as:
            [
                {
                    Sector: XYZ,
                    Companies: [
                                {   code: 123,
                                    company, abc
                                },
                                {   code: 123,
                                    company, abc
                                },
                                ...
                            ]
                },
                {
                    Sector: WXY,
                    Companies: [
                                {   code: 123,
                                    company, abc
                                },
                                {   code: 123,
                                    company, abc
                                },
                                ...
                            ]
                },
                ....
            ]
        '''
        req = requests.get(url, params={})
        soup = BeautifulSoup(req.content, 'html.parser')
        
        # from the response select two classes one for the sector name and the other is its table of companies
        sectorsName = soup.find_all(class_="column-type1 wide vtable offset")
        companysName = soup.find_all(class_="column-type7 wmargin")
        
        # IST_List will hold the final call 
        IST_List = []
        # decide how many sectors are there and loop accordingly
        lenSectors = len(sectorsName)

        for itmIndx in range(lenSectors):        
            record_entry = {} # THISI is the final dictionary to be appended to the IST_LIST
            record_entry["Sector"] = sectorsName[itmIndx].text.replace("\n", "") # FIRST key of the dic hold the sector       
            record_entry["Companies"] = [] # SECOND key in dic that hold the companies, and it's a list to append comps as dic

            codes = companysName[itmIndx].find_all(class_="comp-cell _02 vtable") # list of all available code in that sector
            namesCom = companysName[itmIndx].find_all(class_="comp-cell _03 vtable") # list of all available company name in that sector
            # make sure that the sector has companies other wise just attach str say no companies in this sector
            lenOfEntry = len(codes)
            if lenOfEntry != 0:
                for itm in range(lenOfEntry):
                    temDic = {} # temp dictionary to hold code and company name then append to key ["companies"] for that sector
                    temDic["code"] = codes[itm].text.replace("\n", "")
                    temDic["company"] = namesCom[itm].text.replace("\n", "")
                    record_entry["Companies"].append(temDic)
            else:
                txtNoComFound = "No companies are found in this sector"
                record_entry["Companies"].append(txtNoComFound)

            # as you are done append the record_entry dic to the IST_List
            IST_List.append(record_entry)
        
        # convery that to JSON format and stor it
        try:
            with open("IST_List.json", "w", encoding='utf-8') as final:
                json.dump(IST_List, final, ensure_ascii=False)
        except Exception as e:
            print(f"err {e}")
    


url = "https://www.kap.org.tr/en/Sektorler"
