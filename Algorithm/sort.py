import os,sys
import datetime
from time import localtime,strftime

class Alignment:
    def __init__(self):
        self.dir_list = os.listdir()
        self.dir = os.getcwd()

    #이름
    def sort_name(self,rever):
        # type
        # 오름차순 : False
        # 내림차순 : True
        sort_list = self.dir_list[:]
        sort_list.sort(reverse=rever)
        return sort_list

    #확장자
    def sort_exp(self):
        exp_list = [] #확장자 리스트
        exp_content_list = [] #확장자로 구분한 파일 리스트
        for l in range(len(self.dir_list)):
            exp = os.path.splitext(self.dir_list[l])[1]
            if not (exp in exp_list):
                exp_list.append(exp)
                exp_content_list.append(list())
            
            exp_idx = exp_list.index(exp)
            exp_content_list[exp_idx].append(self.dir_list[l])
        
        return exp_list,exp_content_list

    #수정된 시간기준
    def sort_time(self):
        time_list = list(self.dir_list)
        
        for i in range(0,len(time_list)):
            for j in range(0,len(time_list)):
                before_file = datetime.datetime.fromtimestamp(os.path.getmtime(self.dir+"\\"+time_list[i]))
                after_file = datetime.datetime.fromtimestamp(os.path.getmtime(self.dir+"\\"+time_list[j]))
                if before_file > after_file :
                    (time_list[i], time_list[j]) = (time_list[j], time_list[i])
        
        return time_list

#test
sort_list = Alignment()
print(sort_list.sort_time())