import os

#이름
def sort_name(List,Type):
    # type
    # 오름차순 : false
    # 내림차순 : true
    sort_list = List[:]
    sort_list.sort(reverse=Type)
    return sort_list

#확장자
def sort_exp(List):
    exp_list = [] #확장자 리스트
    exp_content_list = [] #확장자로 구분한 파일 리스트
    for l in range(len(List)):
        exp = os.path.splitext(List[l])[1]
        if not (exp in exp_list):
            exp_list.append(exp)
            exp_content_list.append(list())
        
        exp_idx = exp_list.index(exp)
        exp_content_list[exp_idx].append(List[l])
    
    return exp_list,exp_content_list