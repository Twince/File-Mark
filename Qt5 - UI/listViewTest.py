import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

import os
from PyQt5.QtGui import QIcon, QPixmap



#나중에 함수로 옮겨야 할 거 같은 변수들

display_dir = "";


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("listViewTest.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


        # 기본 설정

        #파일 이름 검색 QLineEdit 엔터 return하면,
        self.DirAddress.returnPressed.connect(self.ShowList) #입력값을 string으로
        self.Btn.clicked.connect(self.FileDialoggy)

        #항목 클릭되었을 떄
        self.LIST.itemClicked.connect(self.ItemClicked)

        

    def createList(self, display_dir):
        print("making table")

        #리스트 항목 초기화
        self.LIST.clear()

        print(display_dir)

        DirIndex = os.listdir(display_dir)
        print(DirIndex)

        self.LIST.addItems(DirIndex)


        
        
            

        # self.LIST = QListWidget(self)
        # item = QListWidgetItem(DirIndex)

        # self.LIST.addTopLevelItem(item)

        
        
       
                

        # list 생성
        # QListWidgetItem(DirIndex)
        

        
        

        #아이템이 클릭됬을때 이벤트
    def ItemClicked(self):
        # print(self.LIST.currentItem().text()) 디버깅 용
        ItemValue = self.LIST.currentItem().text()
        # if "." in ItemValue[-4:]):

        if "." in ItemValue:
            print("File")
        else:
            # print("Folder")
            self.createList(display_dir);

       
        
            




    def FileDialoggy(self):
        display_dir = QFileDialog.getExistingDirectory(self, "Yes") #FileDial은 절대주소 반환
        self.DirAddress.setText(display_dir) #QlineEdit에 주소 표시

        self.createList(display_dir); # list만드는 함수 호출
        
        #same
        

        

        
        #리스트뷰 생성
        

    
    def ShowList(self): #위 str이 text임
        
    
        #same
        display_dir = self.DirAddress.text()
        self.createList(display_dir); # list만드는 함수 호출
    





    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()