import sys
import os

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic

# from PyQt5.QtCore import Qt # 사용되지 않음

# UI 파일 연결
# 단, UI 파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("new start.ui")[0]


def searchFile(path, name=""):
    files = os.listdir(path)
    templist = list()

    for file_name in files:
        if name.lower() in file_name.lower():  # 임시로 모두 소문자로 바꿈 (대소문자 구분없이)
            templist.append(file_name)

    return templist


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 처음 중앙 검색 위치는 프로그램 위치로 설정
        self.fd_cwd = os.getcwd()
        self.FileDir.setText(self.fd_cwd)  # 경로 갱신

        # 파일 이름 검색 QLineEdit 엔터 return 하면,
        self.FileSearch.returnPressed.connect(self.SearchStart)

    # 엔터가 return  됬을때
    def SearchStart(self):
        # 검색한 파일 이름 저장
        Search = self.FileSearch.text()
        print("검색 시작" + str(Search))

        self.treeWidget = QTreeWidget(self)
        self.treeWidget.clear()

        # 검색바 위치 옮기기
        self.FileSearch.move(23, 90)
        # FileMark 라벨 숨김
        self.label.hide()
        # 조건 콤보박스 숨김
        self.comboBox.hide()

        # 트리위젯 초기화
        self.treeWidget.clear()
        # 트리위젯 생성
        self.treeWidget.resize(1090, 500)
        self.treeWidget.move(23, 150)

        # 트리위젯
        self.treeList(Search)

        # 파일 검색 위치
        self.FileDir.returnPressed.connect(self.reSearch)

        # 폴더 항목을 더블 클릭했을 때 그 경로로 검색 위치를 바꿈
        self.treeWidget.itemDoubleClicked.connect(self.reReachSelectedItem)

        self.treeWidget.show()

    def reSearch(self):
        search = self.FileDir.text()
        print("탐색 경로 재 설정!", end="")
        print(search)
        if os.path.isdir(search):   # 새로 입력된 경로가 폴더라면
            self.fd_cwd = search    # 파일 경로로 설정 (파일이라면 찾을게 없음!)

    # 트리 나무 뷰 화면
    def treeList(self, search):
        print("\n\n\n트리 생성")

        # 트리위젯 초기화
        self.treeWidget.clear()

        # 검색할 파일 이름과 비슷한 파일경로 리스트 저장
        searchFileRoutes = searchFile(self.fd_cwd, search)
        self.treeWidget.setHeaderLabels(["파일"])

        # 기본적으로 현재 파일 표시
        for route in searchFileRoutes:
            absName = os.path.join(self.fd_cwd, route)
            treeList = self.newTreeList(absName)
            self.treeWidget.addTopLevelItem(treeList)

        # 항목을 펼칠때 안해 절대
        # self.treeWidget.itemExpanded.connect(self.addList)

    def newTreeList(self, absName):
        # print("\n\n상위 폴더 생성===================================================")
        liName = os.path.basename(absName)

        item = QTreeWidgetItem([liName])  # 상위 항목 생성
        item.setIcon(0, QIcon(QPixmap("Icons\\이동.png")))

        liItems = self.subList(absName)

        # print("하위 폴더 생성=================================")
        # print(liName)
        # print("폴더 생성 list=>" + liItems)
        for subItem in liItems:
            absSubItem = os.path.join(absName, subItem)  # 자식 절대경로 = 부모 절대경로 \ 자식 이름

            # print("\n파일경로 :" + absSubItem)
            # print(str(subItem) + "은 ", end="")

            if os.path.isdir(absSubItem):
                # print("폴더입니다.")
                child = self.newTreeList(absSubItem)
            else:
                # print("파일입니다.")
                child = QTreeWidgetItem([subItem])
                child.setIcon(0, QIcon(QPixmap("Icons\\Copy.png")))

            item.addChild(child)

        return item

    def subList(self, absName):
        liItem = []

        # print(absName)
        if os.path.isdir(absName):
            # print("폴더임.")
            liItem = os.listdir(absName)
        # else:
        #     print("파일임.")
        return liItem

    # 자식의 절대경로를 찾음
    def absChildRoute(self, item):
        route = item.text(0)

        # 부모를 만나면서 경로를 채워감 item은 부모
        while 1:
            parentItem = item.parent()

            if parentItem is not None:  # 부모가 있다면 경로 갱신
                item = parentItem
                parentName = item.text(0)  # 부모 이름 받아옴
                route = os.path.join(parentName, route)
            else:
                # 더 이상 부모가 없다면 탐색 경로 끝까지 온 것이므로 탐색 경로를 붙이고 빠져나옴
                route = os.path.join(self.fd_cwd, route)
                break
        return route

    # 선택된 자식을 탐색함
    def reReachSelectedItem(self):
        curItem = self.treeWidget.currentItem()
        childRute = self.absChildRoute(curItem)
        self.FileDir.setText(childRute)

        self.reSearch()
        self.treeList("")

    # 항목을 펼칠 때 항목 하위 폴더, 파일 추가
    # def addItem(self, IName):
    #
    #     item = QTreeWidgetItem([IName])  # 아이템 항목 생성
    #
    #     if os.path.isdir(IName):    # 폴더인 경우
    #         IList = os.listdir(IName)
    #
    #         for subItem in IList:   # 아이템 하위 항목 추가
    #             child = QTreeWidgetItem([subItem])
    #             item.addChild(child)
    #
    #             self.addItem(subItem)
    #     # 만든 아이템 트리위젯에 추가
    #     self.treeWidget.addTopLevelItem(item)


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass 의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
