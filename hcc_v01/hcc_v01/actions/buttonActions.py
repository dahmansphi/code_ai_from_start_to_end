from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QListWidgetItem
# from DB.dbMain import DbMainCls
from ..DB.dbMain import DbMainCls

class ButtonActionClass:
    def __init__(self):
        super().__init__()
        
    def add_newCase_toDb_toListWidget(self,listWidgetUI,caseP):
        # (1)add to db
        # (2)add to listWidget item
        # (3)clear the current add form
        # (4) print on the err lbl sucess message that will be passed as true or false from the return 
        try:
            # add the case to the database
            inst = DbMainCls()
            inst.insertIntoTable(patientData=caseP)
            lastRecIndxInDb = inst.selectLASTFromTable()
            
            # add the case to the listwidget
            cas_name_num = 'Case num# ' + str(lastRecIndxInDb[0][0])
            icon3 = QIcon()
            icon3.addFile(u":/icons/iconsSVG/person.svg", QSize(), QIcon.Normal, QIcon.Off)
            QlItem = QListWidgetItem(icon3, cas_name_num)
            # add the new item to the list
            listWidgetUI.addItem(QlItem)

            return True
        except:
            return False
           
    def del_itemList_caseDb(self, dbIndx, listWidgetUI):
        try:
            if listWidgetUI.currentItem():
                # delete the item from the Qlistwidget [view_case_widget]
                item_index = listWidgetUI.currentRow()
                listWidgetUI.takeItem(item_index)
                listWidgetUI.clearSelection()
                listWidgetUI.setCurrentRow(-1)
                # delete the case from the db
                inst = DbMainCls()
                inst.deletFromTable(val=dbIndx)             
                return True
        except:
            pass