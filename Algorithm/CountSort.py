
import os

# 디렉토리 이름을 받음 파일 개수를 반환, 파일 이름일 땐 0 반환
def dir_Count(dir_name):
  if os.path.isdir(os.path.abspath(dir_name)): 
    count = len(os.listdir(dir_name))
  else: 
    count = -1

  return count

# 디렉토리 경로, 오름내림차순을 결정할 bool을 받음 디렉토리들의 파일 개수에 따라 정렬해 나온 리스트를 반환, 파일 경로일 땐 빈 리스트 반환
def sort_file_Count(directory_route, rever=True):
  if os.path.isdir(directory_route):
    file_name_list = os.listdir(directory_route)
    file_Count_list = list()

    for file_name in file_name_list:
      file_Count_list.append(dir_Count(file_name))

    file_Count_list.sort(reverse=rever)

    for count in file_Count_list:
      for file_name in file_name_list:
        if count == dir_Count(file_name):
          file_Count_list[file_Count_list.index(count)] = file_name
                    
    return file_Count_list
  else: 
    return list()

# test
#print(sort_file_Count(os.getcwd(), True))