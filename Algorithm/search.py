import os
import shutil
import datetime

class FileSearch:
    def __init__(self,directory_path,search_type,search_word):
        self.dir = os.path.abspath(directory_path)
        self.dir_list = os.listdir(self.dir)
        self.search_list = []
        self.search_word = search_word
        self.search_type = search_type
        self.today = datetime.datetime.today().strftime("%Y-%m-%d")
        self.yesterDay = (datetime.datetime.today() - datetime.timedelta(1)).strftime("%Y-%m-%d")
        self.yesterWeek = (datetime.datetime.today() - datetime.timedelta(7)).strftime("%Y-%m-%d")
        self.yesterMonth = (datetime.datetime.today() - datetime.timedelta(30)).strftime("%Y-%m-%d")        
        self.yesterYear = (datetime.datetime.today() - datetime.timedelta(365)).strftime("%Y-%m-%d")        


    def file_info(self,path):
        infoList = {
            "name" : "",
            "absRoot" : "",
            "ctime" : "",
            "mtime" : "",
            "atime" : "",
            "size" : "",
            "exp" : ""
        }

        if path != "" or (os.path.isdir(path) is False and os.path.isfile(path) is False):
            infoList["name"] = os.path.basename(path)
            infoList["absRoot"] = os.path.abspath(path)
            infoList["size"] = os.path.getsize(path)
            infoList["ctime"] = datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime("%Y-%m-%d")
            infoList["mtime"] = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d")
            infoList["atime"] = datetime.datetime.fromtimestamp(os.path.getatime(path)).strftime("%Y-%m-%d")            
            infoList["exp"] = os.path.splitext(path)[1] if os.path.isfile(path) else ""

        return infoList

    
    def file_search(self,area = ""):
        searchArea = self.dir if area == "" else os.path.join(self.dir,area)
        if os.path.isdir(searchArea):
            search_list = os.listdir(searchArea)
            for data in search_list:
                data = os.path.join(searchArea,data)
                result = self.file_search_detail(data)

                if result:
                    self.search_list.append(self.file_info(data))
                
                if os.path.isdir(data):
                    self.file_search(data)

        return self.search_list

    def file_search_detail(self,data,option = {}):
        searchInfo = self.file_info(data)
        flag = False

        if self.search_type == "name":
            flag = self.search_word in searchInfo["name"]

        if self.search_type == "exp":
            flag = "."+self.search_word in searchInfo["exp"]
        
        if self.search_type == "mtime":
            flag = searchInfo["mtime"]

        return flag
