import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("new start.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox.currentIndexChanged.connect(self.comboBox_event)
        # 파일 이름 검색 QLineEdit 엔터 return하면,
        self.FileSearch.returnPressed.connect(self.SearchStart)

    def comboBox_event(self):
        if self.comboBox.currentIndex() == 0:
            print("검색 시작")

        elif self.comboBox.currentIndex() == 1:
            print("검색 시작")

        elif self.comboBox.currentIndex() == 2:
            print("검색 시작")

        elif self.comboBox.currentIndex() == 3:
            print("검색 시작")

        elif self.comboBox.currentIndex() == 4:
            print("검색 시작")

    # 엔터가 return  됬을때
    def SearchStart(self):
        print("검색 시작")

        # 검색바 위치 옮기기
        self.FileSearch.move(23, 90)
        # FileMark 라벨 없애기
        self.label.deleteLater()
        # 조건 콤보박스 없애기
        self.comboBox.deleteLater()

        # 리스트뷰 생성
        listview = QListView(self)
        listview.setFixedWidth(1090)
        listview.setFixedHeight(500)

        listview.move(23, 150)
        listview.show()


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
