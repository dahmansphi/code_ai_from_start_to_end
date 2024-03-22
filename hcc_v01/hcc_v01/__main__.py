# Copyright (c) 2024 Dr. Deniz Dahman's <denizdahman@gmail.com>
 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# denizdahman@gmail.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

# Support the author of this package on:.#
# https://dahmansphi.com/contact
# https://patreon.com/user?u=118924481
# https://www.youtube.com/@dahmansphi 

import sys
from PySide6.QtWidgets import QApplication
# from ui.mainWindow import MainWindow
from .ui.mainWindow import MainWindow
# from .ui.esseWindow import MainWindow
from PySide6.QtCore import QSize

    
def main():
    # It handles widget specific initialization, finalization
    app = QApplication(sys.argv)
    # this is the main window it is an instance from the ui.mainWindow module
    window = MainWindow()
    window.setFixedSize(QSize(800,500))
    # ***************************************************
    sys.exit(app.exec())

# if __name__ == '__main__':
#     main()