import os

class AAlignment:
  def __init__(self, directory_route):
    self.dir_list = os.listdir(directory_route)

  # 디렉토리들의 파일 개수에 따라 정렬해 나온 리스트를 반환
  def sort_file_Count(self, rever=True):
    sort_dict = dict()

    for li in self.dir_list:
      if os.path.isdir(os.path.abspath(li)):
        file_size = len(os.listdir(li))
      else :
        file_size = -1

      sort_dict[li] = file_size

    sort_list = sorted(sort_dict, key=lambda k: sort_dict[k], reverse=rever)

    return sort_list

# test
sortt = AAlignment(os.getcwd())
print(sortt.sort_file_Count(True))