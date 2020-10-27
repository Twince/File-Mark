import os       # 시스템관련 
import datetime # 시간관련
import time     # 시간관련
import shutil   # 파일연산


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
    def file_info(self):
        names = "C:\\Users\\School\\Desktop\\File-Mark\\Algorithm"
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
            "name" : "",
            "type" : "",
            "absRoot" : "",
            "fileCount" : 0,
            "fileList" : [],
            "ctime" : "",
            "mtime" : "",
            "atime" : "",
            "size" : 0,
            "exp" : ""
        }

        # 이름이 비어있지않는경우 혹은 파일/디렉토리 가 아닌경우
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
        else :
            msg = "ERROR : 파일이 선택되지않음"
        
        return infoList


Fsystem = FileSystem(os.getcwd())
info = Fsystem.file_info()
for key, ans in info.items():
    print(key, " : ",ans)
