
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QLineEdit, QPushButton, QFileDialog
from PyQt6 import QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets
import requests
import pymysql
class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(435, 333)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setEnabled(True)
        font = QtGui.QFont()
        font.setKerning(True)
        self.widget.setFont(font)
        self.widget.setStatusTip("")
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.VideoNameLabel = QtWidgets.QLabel(parent=self.widget)
        palette = QtGui.QPalette()
        self.VideoNameLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoNameLabel.setFont(font)
        self.VideoNameLabel.setObjectName("VideoNameLabel")
        self.gridLayout.addWidget(self.VideoNameLabel, 0, 0, 1, 1)
        self.VideoPathLabel = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoPathLabel.setFont(font)
        self.VideoPathLabel.setObjectName("VideoPathLabel")
        self.gridLayout.addWidget(self.VideoPathLabel, 2, 0, 1, 1)
        self.OpenButton = QtWidgets.QPushButton(parent=self.widget)
        self.OpenButton.setObjectName("OpenButton")
        self.gridLayout.addWidget(self.OpenButton, 6, 0, 1, 1)
        self.SaveButton = QtWidgets.QPushButton(parent=self.widget)
        self.SaveButton.setObjectName("SaveButton")
        self.gridLayout.addWidget(self.SaveButton, 6, 1, 1, 1)
        self.PlayFileButton = QtWidgets.QPushButton(parent=self.widget)
        self.PlayFileButton.setObjectName("PlayFileButton")
        self.gridLayout.addWidget(self.PlayFileButton, 6, 2, 1, 1)
        #self.EncryptButton = QtWidgets.QPushButton(parent=self.widget)
       # self.EncryptButton.setObjectName("EncryptButton")
       # self.gridLayout.addWidget(self.EncryptButton, 6, 3, 1, 1)
      #  self.DecryptButton = QtWidgets.QPushButton(parent=self.widget)
       # self.DecryptButton.setObjectName("DecryptButton")
       # self.gridLayout.addWidget(self.DecryptButton, 6, 4, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 5)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 5)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 0, 1, 5)
        self.EncryptedPath = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.EncryptedPath.setFont(font)
        self.EncryptedPath.setObjectName("EncryptedPath")
        self.gridLayout.addWidget(self.EncryptedPath, 4, 0, 1, 2)
        self.horizontalLayout.addWidget(self.widget)
        self.OpenButton.clicked.connect(self.open_file_dialog)
        self.SaveButton.clicked.connect(self.upload)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.VideoNameLabel.setText(_translate("Dialog", "Video name"))
        self.VideoPathLabel.setText(_translate("Dialog", "Video path"))
        self.OpenButton.setText(_translate("Dialog", "Open"))
        self.SaveButton.setText(_translate("Dialog", "Save to DB"))
        self.PlayFileButton.setText(_translate("Dialog", "Play"))
        #self.EncryptButton.setText(_translate("Dialog", "Encrypt"))
        #self.DecryptButton.setText(_translate("Dialog", "Decrypt"))
        self.EncryptedPath.setText(_translate("Dialog", "Encrypted file path"))
    def open_file_dialog(self):
        file_dialog = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*.*)")
        if file_dialog[0]:
            self.lineEdit_2.setText(file_dialog[0])
    def upload(self):
        file_path = self.lineEdit_2.text()
        url = 'https://192.168.240.26:5000/upload'  # Thay đổi URL nếu server chạy ở địa chỉ khác
        files = {'file': open(file_path, 'rb')}
        print(files)
        try:
            response = requests.post(url, files=files,  verify=False)
            if response.status_code == 200:
                print('File uploaded successfully!')
                self.updatedb()
            else:
                print(f'Error: {response.json().get("error", "Unknown error")}')
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')
    def updatedb(self):
        db = pymysql.connect(host='192.168.240.26',
                                     user='creator',
                                     password='9813',
                                     db='appdb')
        video_name = self.lineEdit.text()
        
        try:
            with db.cursor() as cursor:
            # Kiểm tra xem videoname đã tồn tại hay chưa
                cursor.execute("SELECT COUNT(*) AS count FROM video WHERE videoname = %s", (video_name,))
                result = cursor.fetchone()
                if result and result[0] > 0:
                    print(f'Video name "{video_name}" already exists in the database')
                    return
            
            # Lấy giá trị videoid cao nhất hiện tại
                cursor.execute("SELECT MAX(video_id) AS max_id FROM video")
                result = cursor.fetchone()
                max_id = result[0]
                new_videoid = max_id + 1 if max_id is not None else 1

            # Chèn thông tin video mới vào bảng
                sql = "INSERT INTO video (video_id, videoname) VALUES (%s, %s)"
                cursor.execute(sql, (new_videoid, video_name))
                db.commit()
                print(f'Video {video_name} with ID {new_videoid} added to the database')
        finally:
            db.close()


'''class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400,300)
        self.widget = QtWidgets.QWidget(self)
        main_layout = QHBoxLayout(self.widget)
        self.file_path_line = QLineEdit()
        self.file_path_line.setReadOnly(True)  # Không cho phép chỉnh sửa trực tiếp
      
        # Tạo 3 nút QPushButton
        self.button1 = QPushButton("Play")
        self.button2 = QPushButton("Encrypt")
        self.button3 = QPushButton("Decrypt")
        self.button4 = QPushButton("Open")
        # Thêm các nút vào layout chính
        main_layout.addWidget(self.button1)
        main_layout.addWidget(self.button2)
        main_layout.addWidget(self.button3)
        main_layout.addWidget(self.button4)
        self.button4.clicked.connect(self.open_file_dialog)

        main_layout.addWidget(self.file_path_line);        # Đặt layout chính cho cửa sổ Dialog
        self.setLayout(main_layout)
    def open_file_dialog(self):
        file_dialog = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*.*)")
        if file_dialog[0]:
            self.file_path_line.setText(file_dialog[0]) '''