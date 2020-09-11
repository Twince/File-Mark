import os

#이름
def sort_name(names,reverse):
    # type
    # 오름차순 : false
    # 내림차순 : true
    sort_list = names[:]
    sort_list.sort(reverse=reverse)
    return sort_list

#확장자
def sort_exp(names):
    exp_list = [] #확장자 리스트
    exp_content_list = [] #확장자로 구분한 파일 리스트
    for l in range(len(names)):
        exp = os.path.splitext(names[l])[1]
        if not (exp in exp_list):
            exp_list.append(exp)
            exp_content_list.append(list())
        
        exp_idx = exp_list.index(exp)
        exp_content_list[exp_idx].append(names[l])
    
    return exp_list,exp_content_list