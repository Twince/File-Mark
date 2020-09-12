import os

class Alignment:
    def __init__(self):
        self.dir_list = os.listdir()

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

#test
sort_list = Alignment()
print(sort_list.sort_name(False))