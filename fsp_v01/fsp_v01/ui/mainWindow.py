import os
from PySide6.QtWidgets import QMainWindow
from .ui_window import *
import ftplib
from fsp_v01.config import config
import pandas as pd
import numpy as np
from ..data_centre.dataCentre import DataCentre

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.realTimeGraph = None

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

        # now set the btns to QstackedWidget two pages Add and View case in addtion to clear widget if clicked the btns
        self.ui.view_sector_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.view_sector_page))
        self.ui.view_profile_page_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.view_profile_page))

        self.ui.view_sector_page_btn.clicked.connect(self.clear_view_sectors_widget)
        self.ui.view_sector_page_btn.clicked.connect(self.clear_companies_list_widget)
        
        self.ui.view_profile_page_btn.clicked.connect(self.clear_line_edit_texts)
        # ********************************************************
        # Now move to technical implementation
        # ********************************************************

        # SECTION QListWidget
        # 1. Let's populate the [view_sectors_widget/ QListWidget with all the sectors from the DB]
        self.populate_view_sector_widget()
        # 2. capture the clicked sector in the widget list that have all populated sectors, then populat the relevant companies associated with the sector
        self.ui.view_sectors_widget.itemActivated.connect(self.clicked_item_view_sector_widget)
        self.ui.view_sectors_widget.itemClicked.connect(self.clear_companies_list_widget)

        # BUTTON CLICKED
        self.ui.add_com_to_profile_btn.clicked.connect(self.add_comp_to_profile_btn_clicked)
        self.ui.check_fingerprint_btn.clicked.connect(self.check_fingerPrint_fun)

        self.ui.live_price_chart_btn.clicked.connect(self.live_price_graph)

        self.show()
    # ********* clean list widget and lineEdit ************** #
        
    def clear_line_edit_texts(self):
        img = QPixmap('')
        self.ui.history_price_graph_frame.setPixmap(img)

        self.ui.error_msg_lbl.setText('')
        self.ui.profile_list_widget.clearSelection()
        self.ui.profile_list_widget.setCurrentRow(-1)

        self.ui.add_age.setText('')
        self.ui.add_description.setText('')
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')

        self.ui.add_age.setPlaceholderText('₺00.00')
        self.ui.add_description.setPlaceholderText('₺00.00 - ₺00.00')
        self.ui.lineEdit.setPlaceholderText('00.00 TRY')
        self.ui.lineEdit_2.setPlaceholderText('0.0')

    def clear_companies_list_widget(self):
        self.ui.view_companies_widget.clear()
            
    def clear_companies_selections_rows(self):
        self.ui.view_companies_widget.clearSelection()
        self.ui.view_companies_widget.setCurrentRow(-1)
    def clear_view_sectors_widget(self):
        self.ui.error_msg_lbl.setText('')
        self.ui.view_sectors_widget.clearSelection()
        self.ui.view_sectors_widget.setCurrentRow(-1)

    # ********* Mouse Click Functions ************* #
    def mousePressEvent(self, event):
        '''Listener to mouse press even on the left side'''
        self.clickPosition = event.globalPos()

    # ********** QlistWidget Functions ************* #
    
    def populate_view_sector_widget(self):
        ''' this function populate the view_sector widget will all sectors from the DB'''
        sectors = DataCentre().return_all_sectors()
        if sectors:
            for sector in sectors:
                sector_name = str(sector[1])
                icon3 = QIcon()
                icon3.addFile(u":/icons/iconsSVG/bookmark.svg", QSize(), QIcon.Normal, QIcon.Off)
                QlItem = QListWidgetItem(icon3, sector_name)
                # add the new item to the list
                self.ui.view_sectors_widget.addItem(QlItem)
    
    def clicked_item_view_sector_widget(self):
        '''this function is going to populate the view_companies_widget with relevant companies as the selected sector'''
        # clear the company list widget everytime you click a sector
        self.clear_companies_selections_rows()
        self.clear_companies_list_widget()

        selectedWidgetItemIndx = self.ui.view_sectors_widget.currentRow()
        selectedWidgetItemTxt = self.ui.view_sectors_widget.item(selectedWidgetItemIndx).text()
        dbIndx = int(selectedWidgetItemIndx + 1)
        inst = DataCentre()
        relevant_companies_data = inst.return_relevant_companies(indx=dbIndx)

        companies_list = []
        if relevant_companies_data:
            for comp in relevant_companies_data:
                compIndx = int(comp[0])
                company_info = inst.return_company_give_indx(indx=compIndx)
                
                company_name = company_info[0][1]
                company_code = company_info[0][2]
                companies_list.append([company_code, company_name])
        else:
            no_comp_name = 'No company associated with this sector'
            no_comp_code = 'No code'
            companies_list.append([no_comp_code, no_comp_name])
        
        for itm in companies_list:
            comp_code = itm[0]
            comp_name = itm[1]

            comp_infor = str(comp_code + '||' + '>' + comp_name)
            icon3 = QIcon()
            icon3.addFile(u":/icons/iconsSVG/bookmark.svg", QSize(), QIcon.Normal, QIcon.Off)
            QlItem = QListWidgetItem(icon3, comp_infor)
            # add the new item to the list
            self.ui.view_companies_widget.addItem(QlItem)


    def add_comp_to_profile_btn_clicked(self):
        '''this function add compny to profile_list_widget as the company is slelcted from 
            view_companies_widget, then as it add it remove the item from the copmanies view_copmanies_widget'''

        selectedWidgetItemIndx = self.ui.view_companies_widget.currentRow()
        if selectedWidgetItemIndx != -1:
            selectedWidgetItemTxt = self.ui.view_companies_widget.item(selectedWidgetItemIndx).text()
            if selectedWidgetItemTxt != 'No code||>No company associated with this sector':
                # add it to profile_list_widget then remove it from the current view_companies_widget
                # self.__sessionProfile.append(selectedWidgetItemTxt)
                icon3 = QIcon()
                icon3.addFile(u":/icons/iconsSVG/bookmark.svg", QSize(), QIcon.Normal, QIcon.Off)
                QlItem = QListWidgetItem(icon3, str(selectedWidgetItemTxt))
                self.ui.profile_list_widget.addItem(QlItem)
                
                self.ui.view_companies_widget.takeItem(selectedWidgetItemIndx)

        self.clear_companies_selections_rows()
        
    # view company fingerprint function
    def check_fingerPrint_fun(self):
        self.ui.error_msg_lbl.setText('')
    
        selectedWidgetItemIndx = self.ui.profile_list_widget.currentRow()
        if selectedWidgetItemIndx != -1:
            selectedWidgetItemTxt = self.ui.profile_list_widget.item(selectedWidgetItemIndx).text()
            if selectedWidgetItemTxt == 'THYAO||>TÜRK HAVA YOLLARI A.O.':
                self.ui.add_age.setMaxLength(50)
                self.ui.add_age.setText('₺252.50')
                self.ui.add_description.setText('₺251.50 - ₺256.75')
                self.ui.lineEdit.setText('349.75B TRY')
                self.ui.lineEdit_2.setText('3.70')
                
                img_path = os.getcwd() + '/fsp_v01/ui/' + 'positive_223.jpeg'
                
                img = QPixmap(img_path)
                self.ui.history_price_graph_frame.setPixmap(img)
            else:
                self.clear_line_edit_texts()
                self.ui.error_msg_lbl.setText('For this demo ONLY THYAO is operative')
                
                
    # live price graph
    def live_price_graph(self):
        ''' this function call inst for the realTimemainwindow to graph realtime price but only for thyao '''
        selectedWidgetItemIndx = self.ui.profile_list_widget.currentRow()
        if selectedWidgetItemIndx != -1:
            selectedWidgetItemTxt = self.ui.profile_list_widget.item(selectedWidgetItemIndx).text()
            if selectedWidgetItemTxt == 'THYAO||>TÜRK HAVA YOLLARI A.O.':
                if self.realTimeGraph is None:
                    self.realTimeGraph = RealTimeMainWindow()
                self.realTimeGraph.show()


# Following is the class that is responsible to to plot the realtime price of a company
class MplCanvas(FigureCanvas):
    '''this is a figure canvas that hold the figure and axs'''
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)

        self.fig.patch.set_facecolor('#121416')
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

class RealTimeMainWindow(QMainWindow):
    ''' the class that run the realtime graph'''

    def __init__(self, *args, **kwargs):
        super(RealTimeMainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        self.__mainPathToDataCenter = os.getcwd() + '/fsp_v01/data_centre/' # main path to this model
        self.rt_price = None
        self.fig = self.canvas.fig
        self.ax1 = self.canvas.axes
        self.rt_price_fun()

    def rt_price_fun(self):
        ''' this function will stream the real time price of the code THYAO turkish airline
            it calls the funAnimation
        '''
        ani = FuncAnimation(self.fig, self.animFIGURE, interval=1000, cache_frame_data=False)
        self.canvas.draw()

    def animFIGURE(self,i):
        ''' this is the callback function for the rt_price_fun it basically call the server [denizserver]
            do access to its SERVER_THYAO_RT_PRICE.csv and stream the price on animated figure using matplot
        '''
        try:
            def fileLineCallback(line):
                if line != 'RT_price':
                    self.rt_price = line
                    
            with ftplib.FTP('192.168.123.144',config['username'],config['password']) as ftp:
                ftp.set_pasv(False)
                ftp.retrlines('RETR SERVER_THYAO_RT_PRICE.csv', callback=fileLineCallback)

        except Exception as e:
            self.rt_price = 0.0
            print('connection to server is no success')

        dfTemp = pd.DataFrame()
        price_RT = [np.float64(float(self.rt_price))]

        dfTemp = pd.DataFrame(price_RT,columns=['RT_price'])
        
        dfRTCSV = pd.read_csv(self.__mainPathToDataCenter + 'THYAO_RT_PRICE.csv')

        dfRT = pd.concat([dfRTCSV, dfTemp], ignore_index=True)
        vx = dfRT.index[-1]
        vy = dfRT['RT_price'].tail(1).values[0]
        
        # self.ax1.clear()

        self.ax1.set_xticks([])
        self.ax1.text(0.5, 100.5, 'THYAO_REAL TIME PRICE', color='black', fontsize=18,
                      fontweight='bold', horizontalalignment='left', verticalalignment='center',
                      bbox=dict(facecolor='#FFBF00'))

        tx = f"{vy}"
        self.ax1.annotate(xy=(vx,vy),text=tx,bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3))
        
        self.ax1.ticklabel_format(useOffset=False)
        
        self.ax1.tick_params(axis='both', labelsize=8, colors='white')
        
        self.ax1.plot(dfRT.index, dfRT['RT_price'])



    