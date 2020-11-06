import os

# 지정된 폴더안에 특정 문자가 포함된 파일을 찾는 함수 (대소문자 구분없이)
# path: 탐색할 폴더의 경로, name: 찾고 싶은 문자
def similar(path=os.getcwd(), name=""):
  files = os.listdir(path)
  simlist=[]

  for file_name in files:
    if name.lower() in file_name.lower(): # 임시로 모두 소문자로 바꿈 (대소문자 구분없이)
      simlist.append(file_name)
  
  return simlist

list1 = similar(os.getcwd(), "sort")

print(list1)