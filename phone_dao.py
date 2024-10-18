# 

# 리스트 
file_path = "C:\\javaStudy\\workspace-python\\Phonefile\\PhoneDB.txt"

def read_phonefile(file_path):
    with open(file_path, "r", encoding="utf-8") as person_list:
        for person_vo in person_list:
            person = person_vo.strip().split(",")
            print(f"{person[0]}\t{person[1]}\t{person[2]}")


# 등록
def add_phonefile(file_path):
    with open(file_path, 'r', encoding='utf-8') as person_list:
        p_list = person_list.read() # 전체 내용 읽기
        #print(p_list)

    name = input(">이름: ")
    hp = input(">휴대전화: ")
    company = input(">회사전화: ")

    add = f"{name}, {hp}, {company}\n"

    with open(file_path, 'w', encoding='utf-8') as person_list:
        person_list.write(p_list)   # 원래있던거 적기
        person_list.write(add)      # 새로운 데이터 적기

    print("[등록되었습니다.]")