import os


class NumberCount:
    def __init__(self, directory_path):
        self.dir = os.path.abspath(directory_path)
        self.dir_list = os.listdir(self.dir)

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

    def sort_file_dirfile(self):
        df_list = [[], []]

        for l in self.dir_list:
            if os.path.isdir(l):
                df_list[0].append(l)
            elif os.path.isfile(l):
                df_list[1].append(l)

        return df_list


# test
file_A = NumberCount(os.getcwd())

print("\n포함된 파일 갯수에 따라 정렬된 리스트 :")
print(file_A.sort_file_Count())

print("\n파일 리스트 :")
print(file_A.sort_file_dirfile()[0])
print("\n디렉토리 리스트 :")
print(file_A.sort_file_dirfile()[1])