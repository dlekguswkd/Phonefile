# 전화번호 관리 프로그램

import phone_dao

print("*******************************************")
print("*         전화번호 관리 프로그램          *")
print("*******************************************")

print("1.리스트   2.등록   3.삭제   4.검색   5.종료")
print("--------------------------------------------")

no = int(input(">메뉴번호: "))

if no == 1:
    file_path = "C:\\javaStudy\\workspace-python\\Phonefile\\PhoneDB.txt"
    phone_dao.read_phonefile(file_path)
    



