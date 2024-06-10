
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QListWidgetItem
from PyQt6.QtGui import QIcon, QPixmap
from windows.Dialog import CustomDialog
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
import pymysql
import os
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 591)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStyleSheet("")
      #  MainWindow.setWindowFlag(Qt.WindowMaximizeButtonHint, true)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.central_layout = QVBoxLayout(self.centralwidget)
        self.MainBody = QtWidgets.QWidget(parent=self.centralwidget)
        self.MainBody.setGeometry(QtCore.QRect(234, 9, 581, 573))
        self.MainBody.setObjectName("MainBody")
        self.listWidget = QtWidgets.QListWidget(parent=self.MainBody)
        self.listWidget.setGeometry(QtCore.QRect(5, 71, 571, 481))
        self.listWidget.setObjectName("listWidget")
        self.MenuWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.MenuWidget.setGeometry(QtCore.QRect(9, 9, 221, 573))
        self.MenuWidget.setStyleSheet("background-color: #13131d;\n"
"border:none;\n"
"color:white;")
        self.MenuWidget.setObjectName("MenuWidget")
        self.toolBox = QtWidgets.QToolBox(parent=self.MenuWidget)
        self.toolBox.setGeometry(QtCore.QRect(0, 80, 221, 341))
        self.toolBox.setStyleSheet("#toolBox{\n"
"color:whitel;\n"
"}\n"
"#toolBox::tab{\n"
"padding-left:5px;\n"
"text-align:left;\n"
"border-radius:2px;\n"
"}\n"
"#toolBox::tab:selected{\n"
"background-color:#2d9cdb;\n"
"font-weight:bold;\n"
"}\n"
"#toolBox QPushButton\n"
"{\n"
"padding:5px 0px 5px 20px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"}\n"
"#toolBox QPushButton:hover{\n"
"background-color:#85C1E9;\n"
"}\n"
"#toolBox QPushButton:checked{\n"
"background-color:#4398D8;\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 221, 287))
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HomeButton = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HomeButton.setFont(font)
        self.HomeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.HomeButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
       # self.HomeButton.setIcon(QIcon('../icons/home.png'))
        #icon = QtGui.QIcon()
       # icon.addPixmap(QtGui.QPixmap(":/icon/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off) #C:/Users/Admin/OneDrive/Hình ảnh/App/home.png'''
        #self.HomeButton.setIcon(icon)
     #   self.HomeButton.setIconSize(QtCore.QSize(32, 32))
        self.HomeButton.setCheckable(True)
        self.HomeButton.setAutoExclusive(False)
        self.HomeButton.setObjectName("HomeButton")
        self.verticalLayout.addWidget(self.HomeButton)
        self.HomeButton.setIcon(QIcon(QPixmap(":/icons/home.png")))
        self.HomeButton.setIconSize(QtCore.QSize(32, 32))
        self.AddButton = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddButton.setFont(font)
        self.AddButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AddButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/video-camera.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.AddButton.setIcon(icon1)
        self.AddButton.setIconSize(QtCore.QSize(32, 32))
        self.AddButton.setCheckable(True)
        self.AddButton.setObjectName("AddButton")
        self.AddButton.clicked.connect(self.buttonclicked)
     #   frame = QFileDialog.getOpenFileNames(self, "Open file", "", "All Files (*)")
        self.verticalLayout.addWidget(self.AddButton)
        self.DelButton = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DelButton.setFont(font)
        self.DelButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.DelButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/delete (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.DelButton.setIcon(icon2)
        self.DelButton.setIconSize(QtCore.QSize(32, 32))
        self.DelButton.setCheckable(True)
        self.DelButton.setObjectName("DelButton")
        self.verticalLayout.addWidget(self.DelButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 221, 287))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.UserButton = QtWidgets.QPushButton(parent=self.page_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UserButton.setFont(font)
        self.UserButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/user(1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.UserButton.setIcon(icon3)
        self.UserButton.setIconSize(QtCore.QSize(32, 32))
        self.UserButton.setCheckable(True)
        self.UserButton.setAutoExclusive(False)
        self.UserButton.setObjectName("UserButton")
        self.verticalLayout_2.addWidget(self.UserButton)
        self.AboutButton = QtWidgets.QPushButton(parent=self.page_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AboutButton.setFont(font)
        self.AboutButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.AboutButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.AboutButton.setIcon(icon4)
        self.AboutButton.setIconSize(QtCore.QSize(32, 32))
        self.AboutButton.setCheckable(True)
        self.AboutButton.setAutoExclusive(False)
        self.AboutButton.setObjectName("AboutButton")
        self.verticalLayout_2.addWidget(self.AboutButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.toolBox.addItem(self.page_2, "")
        self.LableTenApp = QtWidgets.QLabel(parent=self.MenuWidget)
        self.LableTenApp.setGeometry(QtCore.QRect(0, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans ExtraBold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.LableTenApp.setFont(font)
        self.LableTenApp.setStyleSheet("color:red;")
        self.LableTenApp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LableTenApp.setObjectName("LableTenApp")
        self.SearchWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.SearchWidget.setGeometry(QtCore.QRect(230, 10, 601, 61))
        self.SearchWidget.setStyleSheet("#SearchWidget{background-color:#ABB2B9;}")
        self.SearchWidget.setObjectName("SearchWidget")
        self.Searchframe = QtWidgets.QFrame(parent=self.SearchWidget)
        self.Searchframe.setGeometry(QtCore.QRect(50, 20, 501, 31))
        self.Searchframe.setStyleSheet("#Searchframe{\n"
"border: 1px solid #aa7e6f;\n"
"border-radius:5px;\n"
"background-color: white;\n"
"}\n"
"QLineEdit { qproperty-frame: false }\n"
"\n"
"#Searchframe QPushButton{\n"
"padding: 5px 5px;\n"
"border-radius:15px;\n"
"}\n"
"#Searchframe QPushButton:pressed{padding-left:10px}\n"
"\n"
"")
        self.Searchframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Searchframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Searchframe.setObjectName("Searchframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Searchframe)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SearchLine = QtWidgets.QLineEdit(parent=self.Searchframe)
        self.SearchLine.setStyleSheet("")
        self.SearchLine.setText("")
        self.SearchLine.setObjectName("SearchLine")
        self.horizontalLayout.addWidget(self.SearchLine)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.Searchframe)
        self.pushButton_5.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/search (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_movies()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("NT219 Secured Streaming", "NT219 Secured Streaming"))
        self.HomeButton.setText(_translate("MainWindow", "Home"))
        self.AddButton.setText(_translate("MainWindow", "Add"))
        self.DelButton.setText(_translate("MainWindow", "Delete"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "General"))
        self.UserButton.setText(_translate("MainWindow", "User"))
        self.AboutButton.setText(_translate("MainWindow", "About"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Setting"))
        self.LableTenApp.setText(_translate("MainWindow", "UitFlix"))
        self.SearchLine.setPlaceholderText(_translate("MainWindow", "Search something..."))
    def buttonclicked(self, s):
        dlg = CustomDialog(self)
        dlg.exec()
    def load_movies(self):
        connection = pymysql.connect(host='192.168.240.26', user='nguoidung', password='9813', db='appdb', port=3306 ,cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "SELECT * FROM video"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                image_blob = row['thumbnail']
                video_path = row['link']
                video_name = row['videoname']
                iconpath = 'content'
                icon = os.path.join(iconpath, f"{video_name}icon.jpg")
                print(os.path.abspath((icon)))
                with open(icon, "wb") as file:
                    file.write(image_blob)
                item = QListWidgetItem()
                self.listWidget.addItem(item)
                item.setIcon((QIcon(QPixmap(icon))))
                self.listWidget.setIconSize(QSize(90, 90))
                item.setText(video_name)  # Không hiển thị văn bản
                item.setData(QtCore.Qt.ItemDataRole.UserRole, video_name)  
    

       
