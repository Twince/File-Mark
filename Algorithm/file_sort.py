import os


class Alignment:
    def __init__(self, directory_path):
        self.now_dir = os.path.abspath(directory_path)
        self.dir_list = os.listdir(self.dir)

    # 이름
    def sort_name(self, rever=False):
        # type
        # 오름차순 : False
        # 내림차순 : True
        sort_list = self.dir_list[:]
        sort_list.sort(reverse=rever)
        return sort_list

    # 확장자
    def sort_exp(self):
        exp_list = []  # 확장자 리스트
        exp_content_list = []  # 확장자로 구분한 파일 리스트
        for l in range(len(self.dir_list)):
            exp = os.path.splitext(self.dir_list[l])[1]
            if not (exp in exp_list):
                exp_list.append(exp)
                exp_content_list.append(list())

            exp_idx = exp_list.index(exp)
            exp_content_list[exp_idx].append(self.dir_list[l])

        return exp_list, exp_content_list

    # 디렉토리들의 파일 개수에 따라 정렬해 나온 리스트를 반환
    def sort_file_Count(self, rever=True):
        sort_dict = dict()

        for li in self.dir_list:
            if os.path.isdir(os.path.abspath(li)):
                file_size = len(os.listdir(li))
            else:
                file_size = -1

        sort_dict[li] = file_size

        sort_list = sorted(sort_dict, key=lambda k: sort_dict[k], reverse=rever)

        return sort_list

    # 디렉토리 이름으로 디렉토리안에 파일 개수를 반환 파일 경로일땐 0
    def dir_Count(self, dir_name):
        if os.path.isdir(self.now_dir):
            count = len(self.dir_list)
        else:
            count = -1

        return count

    # 디렉토리 경로를 받아 그 안에 있는 파일, 디렉토리의 파일 개수에 따라 정렬 파일 경로일땐 빈 리스트 반환
    def sort_file_Count(self):
        if os.path.isdir(self.now_dir):
            file_name_list = self.dir_list[:]
            file_Count_list = list()

            for file_name in file_name_list:
                file_Count_list.append(self.dir_Count())

            file_Count_list.sort(reverse=True)

            for count in file_Count_list:
                for file_name in file_name_list:
                    if count == self.dir_Count():
                        file_Count_list[file_Count_list.index(count)] = file_name

            return file_Count_list
        else:
            return list()
