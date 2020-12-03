import os
import typing

from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *

# UI 파일 연결
# 단, UI 파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
from FileMark.filters import find_ext, contains_name
from FileMark.model import Directory, FileOrDirectory
from FileMark.model.file import finder

# from PyQt5.QtCore import Qt # 사용되지 않음

form_class = uic.loadUiType("FileMark/gui/resources/ui/new start.ui")[0]
SEARCH_FUNCTIONS = {
    0: contains_name,  # 이름
    1: None,  # 날짜
    2: None,  # 크기
    3: find_ext,  # 확장자
    4: None  # 사용빈도
}


def searchFile(path, name=""):
    files = os.listdir(path)
    templist = list()

    for file_name in files:
        if name.lower() in file_name.lower():  # 임시로 모두 소문자로 바꿈 (대소문자 구분없이)
            templist.append(file_name)

    return templist


class FMTreeWidgetItem(QTreeWidgetItem):

    def data(self, column: int, role: int) -> typing.Any:
        data = super().data(column, role)
        if data:
            # print(datetime.now(), self.child(0), column, role, data)
            pass
        return data


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
        filter_func = SEARCH_FUNCTIONS[self.comboBox.currentIndex()]

        self.treeWidget = QTreeWidget(self)
        self.treeWidget.clear()

        # 검색바 위치 옮기기
        self.FileSearch.move(260, 90)
        # FileMark 라벨 숨김
        self.label.hide()
        # 조건 콤보박스 숨김
        self.comboBox.move(20, 90)

        # 트리위젯 초기화
        self.treeWidget.clear()
        # 트리위젯 생성
        self.treeWidget.resize(1090, 500)
        self.treeWidget.move(23, 150)

        # 트리위젯
        self.treeList(Search, filter_func=filter_func)

        # 파일 검색 위치
        self.FileDir.returnPressed.connect(self.reSearch)

        # 폴더 항목을 더블 클릭했을 때 그 경로로 검색 위치를 바꿈
        self.treeWidget.itemDoubleClicked.connect(self.reReachSelectedItem)

        self.treeWidget.show()

    def reSearch(self):
        search = self.FileDir.text()
        print("탐색 경로 재 설정!", end="")
        print(search)
        if os.path.isdir(search):  # 새로 입력된 경로가 폴더라면
            self.fd_cwd = search  # 파일 경로로 설정 (파일이라면 찾을게 없음!)

    # 트리 나무 뷰 화면
    def treeList(self, search, filter_func=None):
        print("\n\n\n트리 생성")

        # 트리위젯 초기화
        self.treeWidget.clear()

        self.reSearch()

        # 검색할 파일 이름과 비슷한 파일경로 리스트 저장
        self.treeWidget.setHeaderLabels(["파일"])
        candidates = searchFile(self.fd_cwd, search)
        if filter_func:
            candidates = filter(lambda x: filter_func(search, finder(os.path.join(self.fd_cwd, x))), candidates)

        for route in candidates:
            absName = os.path.join(self.fd_cwd, route)
            treeList = self.newTreeList(absName)
            self.treeWidget.addTopLevelItem(treeList)

    # 항목의 하위 항목들을 검색해 트리를 생성함
    def newTreeList(self, absName: typing.Union[FileOrDirectory, str]):
        # print("\n\n상위 폴더 생성===================================================")
        now = finder(absName) if isinstance(absName, str) else absName
        item = FMTreeWidgetItem([now.name])  # 상위 항목 생성

        # 파일/ 폴더에 따라 아이콘 변경
        if isinstance(now, Directory):
            item.setIcon(0, QIcon(QPixmap("FileMark/gui/resources/icons/이동.png")))
        else:
            item.setIcon(0, QIcon(QPixmap("FileMark/gui/resources/icons/Copy.png")))

        # print("하위 폴더 생성=================================")
        # print(liName)
        # print("폴더 생성 list=>" + liItems)
        if isinstance(now, Directory):
            for subItem in now.children:  # 하위 항목 리스트 순회
                # print("\n파일경로 :" + absSubItem)
                # print(str(subItem) + "은 ", end="")

                # 하위 항목들 하나하나 트리로 만듦
                child = self.newTreeList(subItem)

                # 생성된 하위 항목 또는 하위 항목의 트리를 상위 항목의 자식으로 추가
                item.addChild(child)

        return item  # 하위 항목들의 탐색을 끝낸 상위 항목을 반환

    # 자식의 절대경로를 찾음
    def absChildRoute(self, item):
        route = item.text(0)

        # 부모를 만나면서 경로를 채워감 item은 현재 부모
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

