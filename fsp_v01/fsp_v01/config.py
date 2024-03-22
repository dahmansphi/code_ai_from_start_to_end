# headers = {
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Encoding':'gzip, deflate, br',
#     'Accept-Language':'en-US,en;q=0.9',
#     'Cache-Control':'max-age=0',
#     'Connection':'keep-alive',
#     'Cookie':'_ga=GA1.1.886546844.1701615627; KAP=AAI7C5hsZTuuF2kBAAAAADsUL9ZOBg_0wi2-O9GbTjIajr9EXp6YjJtEnudHiL6pOw==bpxsZQ==6YI3DFV89PK0RUemTM7-BMd6tTg=; KAP_.kap.org.tr_%2F_wlf=AAAAAAVpJP6JKYNs0PAVtFppXawaMwl_8WKmCUtklFOEGJGCwU0dPY7tbu5k1j2-bD5zPbFUKfUxNs8M_oUby5Scpm8QdsOoBSvPs-9CGJ-_vYvDOg==&; _ga_MBNFVK7SX4=GS1.1.1701615627.1.1.1701615861.49.0.0',
#     'Host':'www.kap.org.tr',
#     'Referer': 'https://www.marketwatch.com/tools/markets/stocks/country/turkey/4',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
#     }

# headers = {
#     'Access-Control-Allow-Origin': '*',
#     'Access-Control-Allow-Methods': 'GET',
#     'Access-Control-Allow-Headers': 'Content-Type',
#     'Access-Control-Max-Age': '3600',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
#     }
config ={
            "username" : 'deniz',
            'password' : 'deniz',
            "insert_INTO_sector_table" : """
                                    INSERT INTO SECTORS
                                    (
                                        SECTOR_NAME
                                    )  
                                    VALUES  (?)
                                    """ ,    

            "insert_INTO_company_table" : """
                                    INSERT INTO COMPANIES
                                    (
                                        COMPPANY_NAME,
                                        COMPPANY_CODE
                                    )  
                                    VALUES  (?,?)
                                    """ ,
                                    
            "insert_INTO_sector_comp_table" : """
                                    INSERT INTO SECTOR_COMP
                                    (
                                        SECTOR_ID,
                                        COMPPANY_ID
                                    )  
                                    VALUES  (?,?)
                                    """  ,
            "select_FROM_sector_table" : """
                                     SELECT id FROM SECTORS WHERE SECTOR_NAME =?
                                    """ ,
            "select_FROM_comp_table" : """
                                     SELECT id FROM COMPANIES WHERE COMPPANY_CODE =?
                                    """ ,
            "select_ALL_FROM_sector_table" : """
                                     SELECT * FROM SECTORS
                                    """ ,
            "select_relevant_COM_FROM_SECTOR_COMP" : """
                                     SELECT COMPPANY_ID FROM SECTOR_COMP WHERE SECTOR_ID =?
                                    """ ,
            "select_compnies_given_indx_FROM_comp_table" : """
                                     SELECT * FROM COMPANIES WHERE id =?
                                    """ 

    }