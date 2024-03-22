import os
from PySide6.QtWidgets import QMainWindow, QFileDialog
from .ui_window import *

from ..actions import listActions, buttonActions
from ..model import model_hcc

import time

class MainWindow(QMainWindow):
    '''
        A main window provides a framework for building an application’s user interface. Qt has QMainWindow and 
        its related classes for main window management. QMainWindow has its own layout to which you can add QToolBar s, 
        QDockWidget s, a QMenuBar , and a QStatusBar . All of which are done using Qt Designer, 
        it instantiates from ui_mainwindow.py
    '''
    __curentCaseSelected_db = None # public var carrys the indx of the case in the db. it's assigend based on the current selected row in QlistWidget
    __dataImgBLOB = None # public var to carry the data img form BLOB to be stored in the db


    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # set the main window to frameless and tranperent background
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

         # activate the close and min button from the customized title bar
        self.ui.close_window_btn.clicked.connect(lambda:self.close())
        self.ui.min_window_btn.clicked.connect(lambda:self.showMinimized())

        # set mainWindow move position that is linked to mosePress event listener
        def moveWindow(e):
            if e.buttons() == Qt.MouseButton.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()
        self.ui.header_frame.mouseMoveEvent = moveWindow

        # set the progressBar vals
        n=100
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(n)

        # now set the btns to QstackedWidget two pages Add and View case
        self.ui.view_case_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.view_case_page))
        self.ui.add_case_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.add_case_page))
        
        # make sure to clear form in case of move between pages
        self.ui.view_case_btn.clicked.connect(self.clearAddCaseFormNextPage)
        self.ui.add_case_btn.clicked.connect(self.clearViewFormNextPage)

        # ********************************************************
        # Now move to technical implementation
        # ********************************************************

        # SECTION QListWidget
        # 1. Let's populate the [view_case_widget/ QListWidget with all the elements from the DB]
        # in the listActions module the function fetchALLDB_populate_listwidge in class ListActionClass will return all 
        # data in the database and pass that data to self.populateListWidget function
        inst_listActionModule = listActions.ListActionClass()
        data_listWidget = inst_listActionModule.fetchAllDB_populate_listwidget()
        self.populateListWidget(data=data_listWidget)

        # 2. Let's capture the clicked item in the list widget [view_case_widget] and pass that clicked to
        # self.selectedListwidgetItem which will strip the name of that item and reach to the last value in the str
        # this value will be ONLY number that refer to the indx in the db
        self.ui.view_case_widget.itemActivated.connect(self.selectedListwidgetItem)
        self.ui.view_case_widget.itemActivated.connect(self.restProgressBar)

        
        # SECTION QPushButton
        #      

        self.ui.del_case_btn.clicked.connect(self.delCaseBtnFun) # delete case btn
        self.ui.add_load_img_btn.clicked.connect(self.loadIMGCaseBtnFun) # load img btn in add new case
        self.ui.add_patient_case_btn.clicked.connect(self.addCaseBtnFun) #  btn in add new case
        self.ui.patient_predict_btn.clicked.connect(self.predictFun)
        self.ui.patient_predict_btn.clicked.connect(self.run)
    
        self.show()

    # ********* Mouse Click Functions ************* #
    def mousePressEvent(self, event):
        '''Listener to mouse press even on the left side'''
        self.clickPosition = event.globalPos()


    # ******* method to run the progress bar in case of prediction *********#
    def run(self):
        n=100
        for i in range(n):
            time.sleep(0.01)
            self.ui.progressBar.setValue(i+1)
    
    def restProgressBar(self):
        self.ui.progressBar.setValue(0)

    # ********* Clear form and lbls Functions ******** #
    def clearAddCaseFormNextPage(self):
        self.ui.add_IMG_idname.setText("") 
        self.ui.add_age.setText("") 
        self.ui.add_description.setText("") 
        self.ui.add_img_thumb_frame.setPixmap(QPixmap(""))
        self.ui.patient_predict_lbl.setText("Model Prediction")
        
        self.ui.error_msg_lbl.setText("")
        self.ui.progressBar.setValue(0)

    def clearViewFormNextPage(self):
        self.ui.patient_IDIMG_data.setText("")
        self.ui.patient_AGE_data.setText("")
        self.ui.patient_stat_data.setText("")
        self.ui.patient_caseDESC_data.setText("")
        self.ui.view_patientIMG_frame.setPixmap(QPixmap(""))
        self.ui.view_case_widget.setCurrentRow(-1)
        self.ui.patient_predict_lbl.setText("Model Prediction")

        self.ui.error_msg_lbl.setText("")
        self.ui.progressBar.setValue(0)

    # ********* QListWidget Functions ************* #
    def populateListWidget(self,data):
        ''' This function works on to populate the qlist widget[view_case_widget].
            it takes arg data and strip that to extract Indx of the case in the db,
            then it strip that and add it to txt [Case num#] as a uniqe number. So when the row is clicked
            this number will be used to select the case from the db based on that indx
        '''
        if data:
            for indx in range(len(data)):
                caseIndxInDb = data[indx][0]
                cas_name_num = 'Case num# ' + str(caseIndxInDb)
                icon3 = QIcon()
                icon3.addFile(u":/icons/iconsSVG/person.svg", QSize(), QIcon.Normal, QIcon.Off)
                QlItem = QListWidgetItem(icon3, cas_name_num)
                # add the new item to the list
                self.ui.view_case_widget.addItem(QlItem)

    def selectedListwidgetItem(self,qlistItem):
        '''
        this function define the current clicked item in the qlist widget [view_case_widget], and 
        works to extract the txt of that item which contain a number at the end of that str. this number 
        indicate the case id in the db. I will use this indx [caseIndxInDb] to fetch the relative data
        of the case such as the age img etc. and pass them to be loaded in the form
        '''
        self.ui.error_msg_lbl.setText("")
        self.ui.patient_predict_lbl.setText("Model Prediction")
        # selectedWidgetItem = ins.selectedWidgetItem(qlistItem=qlistItem)
        selectedWidgetItemIndx = self.ui.view_case_widget.currentRow()
        selectedWidgetItemTxt = self.ui.view_case_widget.item(selectedWidgetItemIndx).text()
        caseIndxInDb = int(selectedWidgetItemTxt.split()[-1])

        # set both publich vars vals. one for the current indx in Listwidget and other val for the case indx in db
        
        self.__curentCaseSelected_db = caseIndxInDb

        # pass that caseIndxDb number to listAction module which will return relevant info about the slected case
        #  from the db, and save the case img to the Asset folder dirc
        ins = listActions.ListActionClass()
        caseSelectedData = ins.selectedWidgetItem(qlistItemSelected=caseIndxInDb)
        # Now you can fill the form of each selected case
        self.ui.patient_IDIMG_data.setText(str(caseSelectedData[0]))
        self.ui.patient_AGE_data.setText(str(caseSelectedData[1]))
        self.ui.patient_caseDESC_data.setText(str(caseSelectedData[2]))
        self.ui.patient_stat_data.setText(str(caseSelectedData[3]))
        # img case 
        # patient_img_temp = os.getcwd()+'/assets/' + 'patientIMG.jpeg' # this is the source of the asset folder
        patient_img_temp = os.getcwd()+'/hcc_v01/assets/' + 'patientIMG.jpeg' # this is the source of the asset folder
# **************
# *************
        img = QPixmap(patient_img_temp)
        self.ui.view_patientIMG_frame.setPixmap(img)

    # ********* QPushButton Functions ************* #

    def predictFun(self):
        isTherCase = self.ui.patient_caseDESC_data.text() == ""
        if isTherCase == False:
            inst = model_hcc.ModelPredict()
            imgPredict = inst.load_image()
            actual_case_stat = self.ui.patient_stat_data.text()

            if imgPredict >= 0.5:
                casePredict = "Ptential Pneumonia: " + str(imgPredict*100) + "%"
                if actual_case_stat == "1":
                    self.ui.error_msg_lbl.setText("Your prediction is RIGHT")
                else:
                    self.ui.error_msg_lbl.setText("Your prediction is WRONG")
            else:
                casePredict = "Ptential Pneumonia: " + str(imgPredict*100) + "%"
                if actual_case_stat == "1":
                    self.ui.error_msg_lbl.setText("Your prediction is WRONG")
                else:
                    self.ui.error_msg_lbl.setText("Your prediction is RIGHT")

            self.ui.patient_predict_lbl.setText(str(casePredict))


    def addCaseBtnFun(self):
        is_imgFormat = type(self.__dataImgBLOB) == bytes
        is_add_IMG_idname = self.ui.add_IMG_idname.text() != ""
        is_age = self.ui.add_age.text() != ""
        is_age_num = self.ui.add_age.text().isnumeric()
        is_description = self.ui.add_description.text() != ""
        is_status = self.ui.add_status.currentText() != ""
        

        isAllTrueList = [is_imgFormat, is_add_IMG_idname,is_age,is_age_num,is_description,is_status]
        isNOTallTrueCondition = False in isAllTrueList

        if isNOTallTrueCondition:
            self.ui.error_msg_lbl.setText("All fields must be filled accordingly")
        
        if is_age_num == False:
            self.ui.error_msg_lbl.setText("Age must be number is not")
        
        if isNOTallTrueCondition == False:
            self.ui.error_msg_lbl.setText("")
            # all are clean and add the case
            caseP = [self.ui.add_IMG_idname.text(), 
                     int(self.ui.add_age.text()), 
                     self.ui.add_description.text(), 
                     self.__dataImgBLOB, 
                     self.ui.add_status.currentIndex()]
            # pass the ready list caseP to buttonActions module that will add it to db and listwidget as new case
            inst = buttonActions.ButtonActionClass()
            caseAddedSucess = inst.add_newCase_toDb_toListWidget(caseP=caseP, listWidgetUI=self.ui.view_case_widget)
            if caseAddedSucess:
                self.clearAddCaseFormNextPage()
                self.ui.error_msg_lbl.setText("The case is added successfuly to DB")
            else:
                self.ui.error_msg_lbl.setText("Something went wrong, case can't be added")
              
    def delCaseBtnFun(self):
        ''' This function to delete the item and the case from the db. it passes the Qlistwidget UI and the public var
            db Indx case based on the current selected row from the QlistWidget
        '''
        ins = buttonActions.ButtonActionClass()
        caseDelInst = ins.del_itemList_caseDb(dbIndx=self.__curentCaseSelected_db, listWidgetUI= self.ui.view_case_widget)
        if caseDelInst:
            self.ui.patient_IDIMG_data.setText("")
            self.ui.patient_AGE_data.setText("")
            self.ui.patient_caseDESC_data.setText("")
            self.ui.patient_stat_data.setText("")
            self.ui.view_patientIMG_frame.setPixmap(QPixmap(""))
            self.ui.error_msg_lbl.setText("The case is successfuly deleted")
    
    def loadIMGCaseBtnFun(self):
        ''' This function responsible to load the case IMG and process it to BLOB ready to be stored in db.
        as well as display the selected imgae into thumbnail display
        '''
        dataIMG = None # data IMG byte BLOB yet to be assigend to it
        file_filter = 'Image File (*.jpeg)' # open dialog box to chose only jpeg imgs
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='select File',
            dir= os.getcwd(),
            filter=file_filter
        )
        img_patient_file = response[0] # this is the path for the img that has been choosen

        if img_patient_file:
            # this condition to make sure that the img that is choosen is not from the asset folder of the project
            # asset_dir = os.getcwd()+'/assets'
            asset_dir = os.getcwd()+'/hcc_v01/assets'
# **************
# **************
            asset_dir = asset_dir.replace('\\','/')
            loadedIMG_dir = (os.path.split(img_patient_file))[0]
            isTrue = loadedIMG_dir == asset_dir
            # confirm the condition to be false in order to accept the img
            if isTrue == False:
                with open(img_patient_file,"rb")as f:
                    dataIMGbytes = f.read()   
                self.ui.error_msg_lbl.setText("")
                dataIMG = dataIMGbytes # Now set the dataIMG var to the bytes form of an img
                
                self.__dataImgBLOB = dataIMG
                imgThumbnail = QPixmap(img_patient_file)
                self.ui.add_img_thumb_frame.setPixmap(imgThumbnail)
                
            else:
                self.ui.error_msg_lbl.setText("You are loading img from asset folder. Please change that. Thank you")
                dataIMG = "None"
                self.__dataImgBLOB = dataIMG
            
        
    # ********* Check Validity ************* #
    