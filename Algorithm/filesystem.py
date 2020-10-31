import os  # 시스템관련
import datetime  # 시간관련
import time  # 시간관련
import shutil  # 파일연산


class FileSystem:
    def __init__(self, directory_path):
        self.dir = os.path.abspath(directory_path)
        self.dir_list = os.listdir(self.dir)
        # 절대주소 값이 안들어오면 현재 디랙토리 값으로 상대 주소

        self.search_option = [True, True]  # search option [0] : 파일 [1] : 디렉토리
        self.select_list = []

    # 파일/디렉토리 삭제
    def file_delete(self, names):
        if names != "":
            if os.path.isdir(names):
                shutil.rmtree(names)
            if os.path.isfile(names):
                os.remove(names)

    # 파일/디렉토리 복사
    def file_copy(self, names):
        # names [0] : 작업을 시행할 파일/디렉토리 [1] : 복사할 이름
        if not (names[0] == "" or names[1] == ""):
            if os.path.isdir(names):
                shutil.copytree(names[0], names[1])
            if os.path.isfile(names):
                shutil.copy(names[0], names[1])
        else:
            msg = "ERROR : 파일이 선택되지않음"
            # System.error(msg) 나중에 System 전용 클래스 만들어서 할 예정

    # 파일/디렉토리 이동
    def file_move(self, names):
        # names [0] : 이동할 파일/디렉토리 [1] : 이동할 위치
        if not (names[0] == "" or names[1] == ""):
            shutil.move(names[0], names[1])
        else:
            msg = "ERROR : 파일이 선택되지않음"

    # 파일/디렉토리 선택
    def file_select(self, names):
        if names != "" and os.path.exists(names):
            if self.select_list in names:
                self.select_list.remove(names)
            else:
                self.select_list.append(names)

    # 파일/디렉토리 정보
    def file_info(self, names):
        # 가져오는 정보 {} 형태는 Dictionary(사전) 자료형이라고 한다. 자세한건 검색바람
        # 이름
        # 종류 (파일 : file / 디렉토리 : dir)
        # 절대경로
        # 포함하는 파일갯수 (default : 0)
        # 포함하는 파일목록 (default : [])
        # 만들어진 시간
        # 최근 변경시간
        # 최근 접근시간
        # 파일크기 (단위 : 바이트)
        # 확장자 (default : "")
        infoList = {
            "name": "",
            "type": "",
            "absRoot": "",
            "fileCount": 0,
            "fileList": [],
            "ctime": "",
            "mtime": "",
            "atime": "",
            "size": 0,
            "exp": ""
        }

        # (이름이 비어있지않는경우 혹은 파일/디렉토리 가 아닌경우)의 not
        if names != "" or (os.path.isdir(names) is False and os.path.isfile(names) is False):
            infoList["name"] = os.path.basename(names)
            infoList["type"] = "dir" if os.path.isdir(names) else "file"
            infoList["absRoot"] = os.path.abspath(names)
            infoList["fileCount"] = len(os.listdir(names)) if os.path.isdir(names) else 0
            infoList["fileList"] = os.listdir(names) if os.path.isdir(names) else []
            infoList["ctime"] = datetime.datetime.fromtimestamp(os.path.getctime(names)).strftime("%Y-%m-%d %H:%M:%S")
            infoList["mtime"] = datetime.datetime.fromtimestamp(os.path.getmtime(names)).strftime("%Y-%m-%d %H:%M:%S")
            infoList["atime"] = datetime.datetime.fromtimestamp(os.path.getatime(names)).strftime("%Y-%m-%d %H:%M:%S")
            infoList["size"] = os.path.getsize(names)
            infoList["exp"] = os.path.splitext(names)[1] if os.path.isfile(names) else ""
        else:
            msg = "ERROR : 파일이 선택되지않음"

        return infoList

    # file_search
    # 기본적으로 현재 디렉토리 기준 모든 하위 요소에 대해 파일/디렉토리 구분하지 않고 검색한다.
    # area : 검색할 위치 (default : 현재 self.dir의 위치)
    # 검색 분류 (OR나 AND 설정)
    # 이름
    # 확장자
    # 특정 날짜기준 [이전/이후/제외/포함]
    # 종류 [파일/디렉토리]
    # 검색어
    def file_search(self, searchList=[], area="", options={
        "name": False,
        "exp": False,
        "date": [False, False],
        "type": False
    }):
        # search data {dataInfo/searchOption/searchContent}
        searchArea = self.dir if area == "" else os.path.join(self.dir, area)

        # dir 검사
        if os.path.isdir(searchArea):
            searchDirList = os.listdir(searchArea)

            for data in searchDirList:
                data = os.path.join(searchArea, data)
                result = self.file_search_detail(area, data, options)

                if result != False:
                    searchList.append(result)

                if os.path.isdir(data):
                    self.file_search(searchList, data, options)
        else:
            msg = "ERORR : 현재 위치에서 실행할 수 없습니다."

        return searchList

    # options 에 맞게 검사
    def file_search_detail(self, folder, data, options):
        name = options["name"]
        exp = options["exp"]
        date = options["date"]
        Type = options["type"]

        searchData = self.file_info(data)
        flag = False
        searchType = []

        # name search
        if name != False and name in os.path.splitext(searchData["name"])[0]:
            flag = True
            searchType.append("name")

        # exp search
        if exp != False and exp in searchData["exp"]:
            flag = True
            searchType.append("exp")

        # type search
        if Type != False and Type == searchData["type"]:
            flag = True
            searchType.append("type")

        # date search
        # date[0] : 비교할 날짜 / date[1] : 비교할 방식 (last,after,except,include)
        if not (False in date):
            compareDate = datetime.datetime.strptime(date[0], "%Y-%m-%d")
            dataDate = datetime.datetime.strptime(searchData["mtime"].split(" ")[0], "%Y-%m-%d")

            if (date[1] == "last" and compareDate > dataDate) or (date[1] == "after" and compareDate < dataDate) or (
                    date[1] == "except" and compareDate != dataDate) or (
                    date[1] == "include" and compareDate == dataDate):
                flag = True
                searchType.append("date - " + data[1])

        if flag:
            searchData["searchType"] = searchType
        else:
            searchData = False

        return searchData


if __name__ == '__main__':
    Fsystem = FileSystem(os.getcwd())
    options = {
        "name": False,
        "exp": False,
        "date": ["2020-10-30", "last"],
        "type": False
    }
    print("검색 결과 : ")
    List = Fsystem.file_search([], "", options)
    if len(List) > 0:
        for data in List:
            print("***")
            print("")
            print("- name : ", data["name"])
            print("- type : ", data["type"])
            print("- absRoot : ", data["absRoot"])
            print("- fileCount : ", data["fileCount"])
            print("- fileList : ", data["fileList"])
            print("- ctime : ", data["ctime"])
            print("- mtime : ", data["mtime"])
            print("- atime : ", data["atime"])
            print("- size : ", data["size"])
            print("- searchType : ", data["searchType"])
            print("")
            print("***")
    else:
        print("없음")
