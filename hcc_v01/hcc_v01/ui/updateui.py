import os
try:
    # os.system("pyside6-uic uiview.ui -o ui_mainwindow.py")
    # os.system("pyside6-rcc icons.qrc -o icons_rc.py")
    
    os.system("pyside6-uic uiview_hcc_v01.ui -o ui_window.py")
    os.system("pyside6-rcc icons.qrc -o icons_rc.py")
    # *********************************
    search_text = "import icons_rc"
    replace_text = "from . import icons_rc"
    # # Input file
    # with open(r'ui_mainwindow.py', 'r') as file:
    with open(r'ui_window.py', 'r') as file: 
        # Reading the content of the file using the read() function and storing them in a new variable 
        data = file.read() 
        # Searching and replacing the text using the replace() function 
        data = data.replace(search_text, replace_text)
    # Opening our text file in write only mode to write the replaced content 
    # with open(r'ui_mainwindow.py', 'w') as file: 
    with open(r'ui_window.py', 'w') as file: 
        # Writing the replaced data in our text file 
        file.write(data)
    # *********************************
    print("Update on the uiview.ui and the icons.qrc is made")
except Exception as e:
    print(f"The update is no success and error detail is {e}")