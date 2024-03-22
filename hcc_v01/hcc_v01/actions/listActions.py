import os
import io
# from DB import dbMain
from PIL import Image
# from DB.dbMain import DbMainCls
from ..DB.dbMain import DbMainCls

class ListActionClass:
    def __init__(self):
        
        super().__init__()

    def  fetchAllDB_populate_listwidget(self):
        inst = DbMainCls()
        data = inst.selectALLFromTable()
        if data:
            return data
                
    def selectedWidgetItem(self, qlistItemSelected):
        ''' this function recieve an indx number from the selectedListwidgetItem function, then use this indx
            to retrieve the data for the selected case. first thing it does (1) it save the img of the case in the
            asset Folder, after removing every other case. (2) it return a list of the case information to be displayed
        '''
        dbInst = DbMainCls().selectFromTable(val=qlistItemSelected) # send to select method in the DB
        # # check if response happens with return then carry out the following
        if len(dbInst) > 0:
        #     # get the image
            for itm in dbInst:
                img = itm[4]      
            # bks the img is blob then use io.ByteIO to decrepit  
            image = Image.open(io.BytesIO(img))

            # patient_img_temp = os.getcwd()+'/assets/' + 'patientIMG.jpeg' # this is the source of the asset folder
# *****************
            patient_img_temp = os.getcwd()+'/hcc_v01/assets/' + 'patientIMG.jpeg'

        #     # clear asset directory from previous img
            # root_dir_asset = os.listdir(os.getcwd()+'/assets/')
#***************
# #***************      
            root_dir_asset = os.listdir(os.getcwd()+'/hcc_v01/assets/')

            if root_dir_asset:
                for f in root_dir_asset:
#  ***********                   
                    # os.remove(os.getcwd()+'/assets/' + f)
                    os.remove(os.getcwd()+'/hcc_v01/assets/' + f)
            
        #     # create the new img and save it to the dirc under the patientIMG.jpeg name
            image.save(patient_img_temp)

        # let's now capsulate the rest of the data in a list and return it 
            selectedCaseDataList = []
            for items in dbInst:
                selectedCaseDataList.append(items[1])
                selectedCaseDataList.append(items[2])
                selectedCaseDataList.append(items[3])
                selectedCaseDataList.append(items[5])
            return selectedCaseDataList


            
   
        