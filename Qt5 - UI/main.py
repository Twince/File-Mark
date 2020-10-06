# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 윈도우 이름 / 크기 설정
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1139, 738)            # 창크기 1139, 738 -> 1140, 740로 변경
        MainWindow.setFixedSize(1140, 740)  # MainWinodw.FixedSize로 창 크기 고정

        # 윈도우 전체 위젯
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 좌측 트리뷰
        self.tree_view = QtWidgets.QTreeView(self.centralwidget)
        self.tree_view.setGeometry(QtCore.QRect(10, 170, 221, 521))
        self.tree_view.setObjectName("tree_view")

        # 홈 / 정렬 탭 위젯 생성
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, 0, 1131, 121))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")

        # 홈 위젯
        self.tab_sort = QtWidgets.QWidget()
        self.tab_sort.setObjectName("tab_sort")

        # 파일 컨트롤을 묶은 그룹박스
        self.file_control_group = QtWidgets.QGroupBox(self.tab_sort)
        self.file_control_group.setGeometry(QtCore.QRect(10, 2, 471, 91))
        self.file_control_group.setObjectName("file_contorl_group")

        # 파일 / 폴더 / 전체 선택하는 드롭박스
        self.type_select = QtWidgets.QComboBox(self.file_control_group)
        self.type_select.setGeometry(QtCore.QRect(10, 18, 91, 21))
        self.type_select.setObjectName("type_select")
        self.type_select.addItem("")
        self.type_select.addItem("")
        self.type_select.addItem("")

        # 이동 버튼
        self.move_btn = QtWidgets.QPushButton(self.file_control_group)
        self.move_btn.setEnabled(False)
        self.move_btn.setGeometry(QtCore.QRect(110, 17, 53, 53))
        self.move_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(path, "Icons/File Move.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)  # 아이콘 표시를 위해 (os.path.join)(path, "아이콘 디렉토리")로 변경
        self.move_btn.setIcon(icon1)
        self.move_btn.setIconSize(QtCore.QSize(50, 50))
        self.move_btn.setObjectName("move_btn")

        # 복사 버튼
        self.copy_btn = QtWidgets.QPushButton(self.file_control_group)
        self.copy_btn.setEnabled(False)
        self.copy_btn.setGeometry(QtCore.QRect(175, 17, 53, 53))
        self.copy_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.join(path, "Icons/Copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_btn.setIcon(icon2)
        self.copy_btn.setIconSize(QtCore.QSize(32, 32))
        self.copy_btn.setObjectName("copy_btn")

        # 붙여넣기 버튼
        self.paste_btn = QtWidgets.QPushButton(self.file_control_group)
        self.paste_btn.setEnabled(False)
        self.paste_btn.setGeometry(QtCore.QRect(240, 17, 53, 53))
        self.paste_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.path.join(path, "Icons/Paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paste_btn.setIcon(icon3)
        self.paste_btn.setIconSize(QtCore.QSize(32, 32))
        self.paste_btn.setObjectName("paste_btn")

        # 삭제 버튼
        self.delete_btn = QtWidgets.QPushButton(self.file_control_group)
        self.delete_btn.setEnabled(False)
        self.delete_btn.setGeometry(QtCore.QRect(305, 18, 53, 53))
        self.delete_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(os.path.join(path, "Icons/Trash can.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon4)
        self.delete_btn.setIconSize(QtCore.QSize(32, 32))
        self.delete_btn.setObjectName("delete_btn")

        # 이름 바꾸기 버튼
        self.name_change_btn = QtWidgets.QPushButton(self.file_control_group)
        self.name_change_btn.setEnabled(False)
        self.name_change_btn.setGeometry(QtCore.QRect(380, 10, 61, 61))
        self.name_change_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(os.path.join(path, "Icons/Change Name.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name_change_btn.setIcon(icon5)
        self.name_change_btn.setIconSize(QtCore.QSize(48, 48))
        self.name_change_btn.setObjectName("name_change_btn")

        # 새 폴더 추가 버튼
        self.new_folder_btn = QtWidgets.QPushButton(self.tab_sort)
        self.new_folder_btn.setGeometry(QtCore.QRect(500, 10, 61, 61))
        self.new_folder_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(path, "Icons/AddNewFolder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_folder_btn.setIcon(icon)
        self.new_folder_btn.setIconSize(QtCore.QSize(48, 48))
        self.new_folder_btn.setObjectName("new_folder_btn")

        # <><><><><><><><><><><><><><><><><><><><><><><><><><><><><<><><><><><><<><><><><><><><><><><><><><>

        # 이동 버튼 레이블
        self.move_label = QtWidgets.QLabel(self.file_control_group)
        self.move_label.setGeometry(QtCore.QRect(123, 70, 31, 16))
        self.move_label.setObjectName("move_label")

        # 복사 버튼 레이블
        self.copy_label = QtWidgets.QLabel(self.file_control_group)
        self.copy_label.setGeometry(QtCore.QRect(190, 70, 31, 16))
        self.copy_label.setObjectName("copy_label")

        # 붙여넣기 버튼 레이블
        self.paste_label = QtWidgets.QLabel(self.file_control_group)
        self.paste_label.setGeometry(QtCore.QRect(242, 70, 51, 16))
        self.paste_label.setObjectName("paste_label")

        # 삭제 버튼 레이블
        self.delete_label = QtWidgets.QLabel(self.file_control_group)
        self.delete_label.setGeometry(QtCore.QRect(319, 70, 31, 16))
        self.delete_label.setObjectName("delete_label")

        # 이름 바꾸기 버튼 레이블
        self.name_change_label = QtWidgets.QLabel(self.file_control_group)
        self.name_change_label.setGeometry(QtCore.QRect(380, 70, 71, 16))
        self.name_change_label.setObjectName("name_change_label")

        # 새 폴더 추가 버튼 레이블
        self.new_folder_label = QtWidgets.QLabel(self.tab_sort)
        self.new_folder_label.setGeometry(QtCore.QRect(494, 73, 71, 16))
        self.new_folder_label.setObjectName("new_folder_label")

        # -------------------------------------------------------------------------------------------------------------------------------------

        # 정렬 탭
        self.tabWidget.addTab(self.tab_sort, "홈")  # ""빈칸을 수정 하여 '홈'을 붙여 디스플레이 시킴
        self.tab_sort = QtWidgets.QWidget()
        self.tab_sort.setObjectName("tab_sort")

        # 선택 정렬 그룹박스(?)
        self.criteria_sort_group = QtWidgets.QGroupBox(self.tab_sort)
        self.criteria_sort_group.setGeometry(QtCore.QRect(0, 1, 211, 81))
        self.criteria_sort_group.setObjectName("criteria_sort_group")
        self.sort_combobox = QtWidgets.QComboBox(self.criteria_sort_group)

        # 정렬 콤보박스
        self.sort_combobox.setGeometry(QtCore.QRect(10, 18, 181, 31))
        self.sort_combobox.setObjectName("sort_combobox")
        self.sort_combobox.addItem("")
        self.sort_combobox.addItem("")
        self.sort_combobox.addItem("")

        # 오름차순 체크박스
        self.up_order = QtWidgets.QCheckBox(self.criteria_sort_group)
        self.up_order.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.up_order.setObjectName("up_order")

        # 내림차순 체크박스
        self.down_order = QtWidgets.QCheckBox(self.criteria_sort_group)
        self.down_order.setGeometry(QtCore.QRect(84, 60, 81, 16))
        self.down_order.setObjectName("down_order")

        # 세부정렬 그룹박스
        self.advanced_sort_group = QtWidgets.QGroupBox(self.tab_sort)
        self.advanced_sort_group.setGeometry(QtCore.QRect(228, 1, 891, 80))
        self.advanced_sort_group.setObjectName("advanced_sort_group")

        # 선택 정렬 버튼
        self.select_sort = QtWidgets.QPushButton(self.advanced_sort_group)
        self.select_sort.setGeometry(QtCore.QRect(10, 15, 75, 55))
        self.select_sort.setObjectName("select_sort")

        self.tabWidget.addTab(self.tab_sort, "")

        # 경로 받는 텍스트 칸(라인에딧)
        self.dir_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.dir_edit.setGeometry(QtCore.QRect(80, 130, 811, 31))
        self.dir_edit.setObjectName("dir_edit")

        # 검색 받는 텍스트 칸(라인에딧)
        self.search_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_edit.setGeometry(QtCore.QRect(902, 130, 191, 31))
        self.search_edit.setObjectName("search_edit")

        # 검색 버튼
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(1092, 129, 38, 33))
        self.search_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon6)
        self.search_btn.setObjectName("search_btn")

        # 뒤로가기 버튼
        self.undo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.undo_btn.setGeometry(QtCore.QRect(10, 130, 31, 31))
        self.undo_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo_btn.setIcon(icon7)
        self.undo_btn.setObjectName("undo_btn")

        # 앞으로 가기 버튼
        self.redo_btn = QtWidgets.QPushButton(self.centralwidget)
        self.redo_btn.setGeometry(QtCore.QRect(40, 130, 31, 31))
        self.redo_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/Foward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redo_btn.setIcon(icon8)
        self.redo_btn.setObjectName("redo_btn")

        # 우측 리스트 뷰
        self.list_view = QtWidgets.QListView(self.centralwidget)
        self.list_view.setGeometry(QtCore.QRect(240, 170, 891, 521))
        self.list_view.setObjectName("list_view")

        MainWindow.setCentralWidget(self.centralwidget)

        # 상단 메뉴바
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1139, 21))
        self.menubar.setObjectName("menubar")

        # ㄴ>
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)

        # 상태바
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # To be contiuned, (상단 메뉴바 -> 설정 -> 투비 컨틴뉴 메뉴)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 번역/
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "파일 마크 - FileMark"))  # MainWindow(폼 타이틀)를 '파일 마크 - FileMark로 변경
        self.tree_view.setStatusTip(_translate("MainWindow", "Tree View"))
        self.new_folder_btn.setToolTip(_translate("MainWindow", "새로운 폴더 생성"))
        self.new_folder_btn.setStatusTip(_translate("MainWindow", "새로운 폴더 생성"))
        self.file_control_group.setTitle(_translate("MainWindow", "파일 컨트롤"))
        self.type_select.setItemText(0, _translate("MainWindow", "전체"))
        self.type_select.setItemText(1, _translate("MainWindow", "폴더"))
        self.type_select.setItemText(2, _translate("MainWindow", "파일"))
        self.copy_btn.setToolTip(_translate("MainWindow", "복사"))
        self.paste_btn.setToolTip(_translate("MainWindow", "붙여넣기"))
        self.move_label.setText(_translate("MainWindow", "이동"))
        self.copy_label.setText(_translate("MainWindow", "복사"))
        self.paste_label.setText(_translate("MainWindow", "붙여넣기"))
        self.delete_label.setText(_translate("MainWindow", "삭제"))
        self.name_change_label.setText(_translate("MainWindow", "이름 바꾸기"))
        self.new_folder_label.setText(_translate("MainWindow", "새 폴더 추가"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sort),
                                  _translate("MainWindow", "홈"))  # self.widget을 (탭 위젯에 첫번째 탭) tab_sort로 수정하여 오류해결
        self.criteria_sort_group.setTitle(_translate("MainWindow", "기본 정렬"))
        self.sort_combobox.setItemText(0, _translate("MainWindow", "이름순"))
        self.sort_combobox.setItemText(1, _translate("MainWindow", "파일 확장자"))
        self.sort_combobox.setItemText(2, _translate("MainWindow", "파일 크기"))
        self.up_order.setToolTip(_translate("MainWindow", "기본으로 오름차순으로 설정되어 있음"))
        self.up_order.setText(_translate("MainWindow", "오름차순"))
        self.down_order.setText(_translate("MainWindow", "내림차순"))
        self.advanced_sort_group.setTitle(_translate("MainWindow", "세부 정렬"))
        self.select_sort.setText(_translate("MainWindow", "선택정렬"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sort), _translate("MainWindow", "정렬"))
        self.list_view.setStatusTip(_translate("MainWindow", "ListView"))
        self.menu.setTitle(_translate("MainWindow", "설정"))
        self.action.setText(_translate("MainWindow", "To be contiuned..."))


if __name__ == "__main__":
    import sys
    import os  # icon 상대적 파일 경로를 위해 os 를 import함

    path = os.path.dirname(os.path.abspath(__file__))  # icon path

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
