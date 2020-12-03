import os


class Remake:
    def __repr__(self):
        return "<Remake name={} result={}>".format(self.name, self.result)

    def __init__(self, price):
        self.name = ""
        self.result = 0
        self.price = price

    def input(self, path):
        self.name = path
        self.result = File_size

        return self.result

    def __lt__(self, other):
        return self.price < other.price


# 단위별 분할(사용자 편의상 출력할때만 호출)
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
        print(num)


if __name__ == '__main__':
    File_List = os.listdir()
    ReSorted_List = []

    # 해당 파일주소의 파일용량 색출 후 클래스로 인풋
    for i in range(len(File_List)):
        File_path = File_List[i]
        File_size = os.stat(File_path).st_size

        ReSorted_List.append(Remake(File_size))
        ReSorted_List[i].input(File_path)

    ReSorted_List.sort()
    print(ReSorted_List)  # 반환값은 name과 용량(byte 단위)
